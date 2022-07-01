from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('create/', views.create, name='create'),
    path('validate_login/', views.create, name='validate_login'),
]