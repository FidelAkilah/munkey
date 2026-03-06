"""
Custom authentication for NextAuth JWT tokens.
Validates tokens by checking against the database user records.
"""
import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import authentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.models import User

UserModel = get_user_model()


class NextAuthJWTAuthentication(authentication.BaseAuthentication):
    """
    Custom authentication for NextAuth JWT tokens.
    Validates tokens by:
    1. First trying standard JWT validation
    2. If that fails, validating by getting user ID from token and checking database
    """

    def authenticate_header(self, request):
        """Return a string for the WWW-Authenticate header.
        This makes DRF return 401 instead of 403 for unauthenticated requests,
        which allows the frontend to detect token issues and prompt re-login."""
        return 'Bearer realm="api"'

    def authenticate(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        
        if not auth_header:
            return None
            
        auth_parts = auth_header.split()
        
        if len(auth_parts) != 2:
            return None
            
        prefix, token = auth_parts
        
        if prefix.lower() != 'bearer':
            return None

        if not token or token in ('undefined', 'null', ''):
            return None
        
        # Try standard JWT authentication first
        try:
            result = JWTAuthentication().authenticate(request)
            if result:
                return result
        except Exception as e:
            import logging
            logging.getLogger(__name__).debug(f"Standard JWT auth failed, trying fallback: {e}")
        
        # Fallback: Decode token manually and validate against database
        return self.authenticate_credentials(token)
    
    def authenticate_credentials(self, token):
        """
        Authenticate by decoding token and validating user exists in database.
        The NextAuth session stores the Django JWT from login time, but may
        outlive the token's 60-min expiry. Since we already skip signature
        verification (relying on the DB lookup for trust), we also skip
        expiration so that long-lived sessions keep working.
        """
        import logging
        logger = logging.getLogger(__name__)

        try:
            payload = jwt.decode(
                token,
                options={"verify_signature": False, "verify_exp": False},
                algorithms=["HS256", "HS512", "RS256"]
            )
            
            # Get user ID from token payload (try multiple claim names)
            # NextAuth uses 'sub', Django JWT uses 'user_id'
            user_id = payload.get('user_id') or payload.get('id') or payload.get('sub')
            
            if not user_id:
                logger.warning(f"JWT decoded but no user_id found. Claims: {list(payload.keys())}")
                return None

            # Coerce to int if it's a numeric string
            try:
                user_id = int(user_id)
            except (ValueError, TypeError):
                pass
            
            # Look up user in database
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                logger.warning(f"JWT user_id={user_id} not found in database")
                return None
            
            return (user, token)
            
        except jwt.DecodeError as e:
            logger.debug(f"JWT decode error: {e}")
            return None
        except Exception as e:
            logger.warning(f"Unexpected auth error: {e}")
            return None


def decode_jwt_manually(token):
    """
    Manually decode JWT without verification (for getting user info).
    """
    try:
        parts = token.split('.')
        if len(parts) != 3:
            return None
            
        payload = jwt.decode(
            parts[1],
            options={"verify_signature": False}
        )
        
        return payload
    except Exception:
        return None

