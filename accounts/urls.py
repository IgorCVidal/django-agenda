from os import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='index_login'),
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('dashboard/', views.dashboard, name='dashboard'),
]