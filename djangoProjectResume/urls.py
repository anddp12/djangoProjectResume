from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('resume', include('main.urls')),
    path('contact', include('main.urls')),
]
