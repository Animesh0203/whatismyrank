from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('login/', views.login_view, name='login'),  
    #path('register/', views.create, name='register'),
    path('logout/', views.logout_view, name='logout'), 
    path('register/', views.register_user, name='register_user'),
]
