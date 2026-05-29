from django.contrib import admin
from django.urls import path, include   # ← ты уже это используешь

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]