from django.urls import path
from .views import ResetPasswordView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('login/', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'), 
    path('register/', views.register_user, name='register_user'),
    path('submit/',views.get_id,name='submit'),
    path('recoverpassword/',ResetPasswordView.as_view()),
    
    path('password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='mainapp/password_reset_confirm.html'),
         name='password_reset_confirm'),
    
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='mainapp/password_reset_complete.html'),
         name='password_reset_complete'),
    
    path('games/<int:game_id>/', views.games, name='games')
]
