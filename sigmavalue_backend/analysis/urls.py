# sigmavalue_backend/analysis/urls.py

from django.urls import path
from .views import analyze_view

urlpatterns = [
    path("analyze/", analyze_view, name="analyze"),     # /api/analyze/
]
