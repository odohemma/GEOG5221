"""stations URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from retailers.views import RegistrationView, ProfileView, UserDelete

urlpatterns = [
    #URL to visit the site's admin page.
    path('admin/', admin.site.urls),

    #URL to get JSON of selected fields the site's database.
    path("api/", include("retailers.api")),

    #URL to visit the site's homepage
    path('', include("retailers.urls"), name='retailers'),

    #URLs to register new retailer, view retailer's profile, login and logout a retailer. 
    path('retailers/register/', RegistrationView.as_view(), name='register'),
    path('retailers/profile/', ProfileView.as_view(), name='profile'),
    path('retailers/login/', auth_views.LoginView.as_view(), name='login'),
    path('retailers/logout/', auth_views.LogoutView.as_view(), name='logout'),

    #URLs to change password and confirm password change of a retailer's account.
    path('retailers_change_password/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('retailers_change_password/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    #URLs to reset password of a retailer's account.
    path('retailers_reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('retailers_reset_password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('retailers_reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('retailers_reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    #URL to delete a retailer's account.
    path('<int:pk>/delete', UserDelete.as_view(), name='user_confirm_delete'),
]
