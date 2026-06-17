from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from meme import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('meme.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='meme/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)