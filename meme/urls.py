from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('add_meme/', views.add_meme, name='add_meme'),
    path('contact/', views.contact, name='contact'),
    path('like/<int:pk>/', views.like_meme, name='like_meme'),
    path('delete/<int:meme_id>/', views.delete_meme, name='delete_meme'),
    path('signup/', views.signup, name='signup'),
]