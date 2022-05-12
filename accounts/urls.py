from django.urls import path
from .views import LoginPage, logout_page, UserProfile, UserUpdate, SignUpPage, UserList

urlpatterns = [
    path('signup', SignUpPage.as_view(), name = 'signup'),
    path('login/', LoginPage.as_view(), name = 'login_page'),
    path('logout/', logout_page, name = 'logout_page'),
    path('profile', UserProfile.as_view(), name = 'profile'),
    path('profile-update/<int:pk>', UserUpdate.as_view(), name = 'profile_update'),
    path('user-list', UserList.as_view(), name = 'user_list')
]