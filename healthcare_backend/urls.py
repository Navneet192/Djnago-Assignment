from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("users.urls")), 
    path('api/', include('patients.urls')),
    path('api/', include('doctors.urls')),
    path('api/mappings/', include('mappings.urls')),
]
