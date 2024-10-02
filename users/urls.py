from django.urls import path
from .import views
from django.contrib.auth import views as auth_view

urlpatterns = [
     path('sign_up/', views.sign_up, name='users-sign-up'),
     path('profile/', views.profile, name='users-profile'),
     path('', auth_view.LoginView.as_view(
               template_name='users/login.html',
               success_url='blog/'), 
               name='users-login'),
     path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'),
          name='users-logout'),
     path('password_reset/', views.password_reset_request, name='password_reset'),
     path('password_reset_done/', views.password_reset_done, name='password_reset_done'),
     path('password_reset_confirm/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
     path('password_reset_complete/', views.password_reset_complete, name='password_reset_complete'),
    ]