from rest_framework.viewsets import ModelViewSet
from rest_framework_gis.filters import InBBOXFilter

from .models import Report
from .serializers import ReportSerializer


class ReportViewSet(ModelViewSet):
    queryset = Report.objects.all()
    bbox_filter_field = "location"
    filter_backends = (InBBOXFilter,)
    serializer_class = ReportSerializer