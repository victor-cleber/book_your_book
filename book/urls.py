from django.urls import path
from . import views # referencia a propria pasta - book

urlpatterns = [
    path('create/', views.create),
    path('home/', views.home, name='home'),
    path('ver_livro/<int:id>', views.ver_livro, name='ver_livro'),

]