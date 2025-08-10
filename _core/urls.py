from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path("", include("_essential.urls")),
  path('admin/', admin.site.urls),
  path("example/", include("example.urls")),
]
