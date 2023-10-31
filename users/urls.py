from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('login/', views.login_request, name = 'login_request'),
    path('logout/', views.logout_request, name = 'logout_request'),
    path('profile/', views.profile_view, name = 'profile'),
]