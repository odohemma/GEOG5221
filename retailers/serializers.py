from rest_framework_gis import serializers

from .models import Retailer


class RetailerSerializer(serializers.GeoFeatureModelSerializer):
    """Retailer GeoJSON serializer."""

    class Meta:
        """Retailer serializer meta class."""

        fields = ("id", "name", "phone","pms_rate","pms_stock","ago_rate","ago_stock","dpk_rate","dpk_stock","lpg_rate","lpg_stock", "auto_shop", "supermart")
        geo_field = "coordinates"
        model = Retailer