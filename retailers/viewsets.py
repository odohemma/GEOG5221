from rest_framework import viewsets
from rest_framework_gis import filters

from .models import Retailer
from .serializers import RetailerSerializer


class RetailerViewSet(viewsets.ReadOnlyModelViewSet):
    """Retailer view set."""

    bbox_filter_field = "coordinates"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Retailer.objects.all()
    serializer_class = RetailerSerializer