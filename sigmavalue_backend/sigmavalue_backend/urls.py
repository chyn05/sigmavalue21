# sigmavalue_backend/sigmavalue_backend/urls.py

from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse


def health_check(request):
    return JsonResponse({"status": "ok", "message": "Sigmavalue backend is running."})


urlpatterns = [
    path("", health_check, name="health_check"),        # GET /
    path("admin/", admin.site.urls),                    # /admin/
    path("api/", include("analysis.urls")),             # /api/...
]
