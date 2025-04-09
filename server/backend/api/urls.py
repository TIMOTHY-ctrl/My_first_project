from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, LoginView, RefreshTokenView, UserListView, IssueListView, IssueDetailView, NotificationListView

urlpatterns = [
    # JWT Token endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # User registration and login
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', RefreshTokenView.as_view(), name='token_refresh_custom'),

    # User-related endpoints
    path('users/', UserListView.as_view(), name='user_list'),

    # Issue-related endpoints
    path('issues/', IssueListView.as_view(), name='issue_list'),
    path('issues/<int:pk>/', IssueDetailView.as_view(), name='issue_detail'),

    # Notification-related endpoints
    path('notifications/', NotificationListView.as_view(), name='notification_list'),
]