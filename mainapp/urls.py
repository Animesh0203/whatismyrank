from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.homepage),
    path('submit/',views.get_id,name='submit'),

]
