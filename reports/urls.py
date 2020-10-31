from django.urls import path
from rest_framework.routers import DefaultRouter
from .api import ReportViewSet


router = DefaultRouter()
app_name = "reports"

router.register("report_json", ReportViewSet, basename="report_json")

urlpatterns = router.urls
