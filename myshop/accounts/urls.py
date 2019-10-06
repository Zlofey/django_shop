from django.urls import path, include
from accounts.views import signup, profile_view, profile_change, password_edit


app_name = 'accounts'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('profile/', profile_view, name='profile_view'),
    path('profile_change/', profile_change, name='profile_change'),
    path('password_edit/', password_edit, name='password_edit'),
    path('', include('django.contrib.auth.urls')),

]