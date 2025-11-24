from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def health_check(request):
    return JsonResponse({"status": "ok", "message": "Sigmavalue backend is running."})

urlpatterns = [
    path("", health_check, name="health_check"),  # 👈 root path
    path("admin/", admin.site.urls),
    path("api/", include("analysis.urls")),
]
