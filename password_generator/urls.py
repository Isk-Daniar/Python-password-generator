from django.urls import path
from generator import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('generatedpassword/', views.password, name='password'),
    path('info', views.info, name='info'),
]
