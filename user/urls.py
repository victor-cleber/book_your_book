from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('create/', views.create, name='create'),
    path('valida_cadastro/', views.valida_cadastro, name='valida_cadastro'),
    path('valida_login/', views.valida_login, name='valida_login'),
]