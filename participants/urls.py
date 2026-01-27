from django.urls import path
from . import views


app_name = "participants"

urlpatterns = [
    path('', views.home, name='home'),           # Front page
    path('login/', views.participant_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.participant_logout, name='logout'),
]
