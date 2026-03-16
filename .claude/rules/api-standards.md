# API Standards — Django REST Framework

## Endpoint Structure
- All endpoints are prefixed with `/api/`
- Use Django REST Framework ViewSets or APIViews (class-based)
- URL patterns defined per-app in `<app>/urls.py`, included in `core/urls.py`

## Serializers
- Every endpoint must use a DRF Serializer for input validation and output formatting
- Keep serializers in `<app>/serializers.py`
- Use `ModelSerializer` for standard CRUD, `Serializer` for custom logic

## Authentication & Permissions
- Use `IsAuthenticated` permission for protected endpoints
- JWT tokens validated via `NextAuthJWTAuthentication` in `core/authentication.py`
- Custom permissions go in the app's `permissions.py` if needed
- Admin-only endpoints should check `request.user.role == 'AD'`

## Response Format
- Return standard DRF responses (serializer data + status codes)
- Use appropriate HTTP status codes: 200, 201, 400, 401, 403, 404, 429
- Error responses should include descriptive messages
- 429 responses include `{"error": "Rate limit exceeded", "retry_after": <seconds>}` plus `Retry-After` header

## Rate Limiting
- DRF throttling configured in `core/settings.py` → `REST_FRAMEWORK['DEFAULT_THROTTLE_CLASSES']`
- Custom throttle classes in `core/throttling.py`: `AIEndpointThrottle`, `AuthEndpointThrottle`, `NewsCreateThrottle`, `CommentPostThrottle`, `DefaultUserThrottle`
- `DefaultUserThrottle` (100/min) applies globally; override with specific throttle classes per view
- AI endpoints must use `AIEndpointThrottle` (20/hour) and call `check_daily_token_limit()` before OpenAI calls
- Auth endpoints use `AuthEndpointThrottle` (5/min per IP) — throttled wrappers in `core/views.py`
- Throttle rates defined in `REST_FRAMEWORK['DEFAULT_THROTTLE_RATES']` in settings
- Custom exception handler `core.throttling.custom_exception_handler` formats 429 responses with JSON body + headers
- All responses expose `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`, `Retry-After` headers via `CORS_EXPOSE_HEADERS`

## CORS
- Allowed origins: `https://munkey-zeta.vercel.app`, `http://localhost:3000`
- Update `CORS_ALLOWED_ORIGINS` in `core/settings.py` when adding new frontend URLs
- `CORS_EXPOSE_HEADERS` includes rate limit headers — update if adding new custom response headers

## Database
- PostgreSQL via Supabase (pooled connection on port 6543)
- Always create and run migrations after model changes
- Use Django's ORM — no raw SQL unless absolutely necessary

## File Uploads
- PDF text extraction via `pypdf` in `curriculum/ai_service.py`
- Validate file types server-side before processing
- Never store uploaded files with user-supplied filenames directly
