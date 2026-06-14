from django.urls import path
from . import views

urlpatterns = [
    path('', views.english),
    path('fr/', views.french),
    path('de/', views.german),
    path('es/', views.spanish),
]