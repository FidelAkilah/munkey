# Article Submission and Review System Implementation

## Backend - Database Changes
- [x] 1.1 Add status field to Article model (PENDING, APPROVED, REJECTED)
- [x] 1.2 Create migration
- [x] 1.3 Run migration

## Backend - API Views & Serializers
- [x] 2.1 Update ArticleSerializer to include status field
- [x] 2.2 Modify ArticleListView to only show APPROVED articles (public)
- [x] 2.3 Modify ArticleCreateView to allow any authenticated user
- [x] 2.4 Add AdminArticleReviewView with pending/approve/reject endpoints
- [x] 2.5 Add proper permissions (IsAuthenticated, IsAdminUser)

## Backend - URL Routing
- [x] 3.1 Add admin review endpoints to news/urls.py

## Frontend - Authentication
- [x] 4.1 Update auth.ts to include role in session
- [x] 4.2 Create AuthProvider for session context

## Frontend - Navbar
- [x] 5.1 Check authentication state
- [x] 5.2 Show "Login" if not authenticated
- [x] 5.3 Show user menu with "My Submissions" if logged in
- [x] 5.4 Show "Admin Dashboard" link if user is admin
- [x] 5.5 Hide "Add News" button if not logged in

## Frontend - Add News Page
- [x] 6.1 Update to show submission success message
- [x] 6.2 Add loading states and error handling

## Frontend - Homepage
- [x] 7.1 Replace email submission with link to /news/add
- [x] 7.2 Update text to reflect new submission process

## Additional Pages Created
- [x] /news/my-articles/ - User's submitted articles with status
- [x] /admin/dashboard/ - Admin review interface for pending articles

## Testing
- [ ] 8.1 Test article submission as regular user
- [ ] 8.2 Test article approval as admin
- [ ] 8.3 Test that only approved articles appear publicly

