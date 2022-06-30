from django.urls import path
from . import views # referencia a propria pasta - book

urlpatterns = [
    path('create/', views.create)
]