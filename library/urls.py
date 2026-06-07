from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('writers/', views.writers, name='writers'),
    path('books/', views.books, name='books'),

    path('writers/<str:name>/', views.writer_detail, name='writer_detail'),
    path('books/<str:title>/', views.books_detail, name='books_detail'),
]