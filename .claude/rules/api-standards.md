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
- Use appropriate HTTP status codes: 200, 201, 400, 401, 403, 404
- Error responses should include descriptive messages

## CORS
- Allowed origins: `https://munkey-zeta.vercel.app`, `http://localhost:3000`
- Update `CORS_ALLOWED_ORIGINS` in `core/settings.py` when adding new frontend URLs

## Database
- PostgreSQL via Supabase (pooled connection on port 6543)
- Always create and run migrations after model changes
- Use Django's ORM — no raw SQL unless absolutely necessary

## File Uploads
- PDF text extraction via `pypdf` in `curriculum/ai_service.py`
- Validate file types server-side before processing
- Never store uploaded files with user-supplied filenames directly
