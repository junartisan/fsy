from django.urls import path
from . import views

app_name = "participants"

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.participant_login, name='login'), # Called via participants:login
    path('dashboard/', views.dashboard, name='dashboard'), # Called via participants:dashboard
    path('logout/', views.participant_logout, name='logout'),
    path('register/', views.participant_register, name='register'), # Changed 'participant_register' to 'register' for simplicity
]