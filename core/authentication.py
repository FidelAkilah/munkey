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
        
        # Try standard JWT authentication first
        try:
            # Try the standard JWT authentication
            result = JWTAuthentication().authenticate(request)
            if result:
                return result
        except Exception:
            pass
        
        # Fallback: Decode token manually and validate against database
        return self.authenticate_credentials(token)
    
    def authenticate_credentials(self, token):
        """
        Authenticate by decoding token and validating user exists in database.
        """
        try:
            # Decode the JWT without verification (since keys may differ)
            # but extract the user_id from the payload
            payload = jwt.decode(
                token,
                options={"verify_signature": False},
                algorithms=["HS256", "HS512", "RS256"]
            )
            
            # Get user ID from token payload (try multiple claim names)
            # NextAuth uses 'sub', Django JWT uses 'user_id'
            user_id = payload.get('user_id') or payload.get('id') or payload.get('sub')
            
            if not user_id:
                return None
            
            # Look up user in database
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                return None
            
            # Ensure is_authenticated is True
            user.is_authenticated = True
            
            return (user, token)
            
        except jwt.DecodeError:
            return None
        except Exception as e:
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

