from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('writers/', views.writers, name='writers'),
    path('books/', views.books, name='books'),
]