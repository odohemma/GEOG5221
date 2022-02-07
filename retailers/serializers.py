from rest_framework_gis import serializers

from .models import Retailer


class RetailerSerializer(serializers.GeoFeatureModelSerializer):
    """This class enables the creation of GeoJSON for the Retailer table."""

    class Meta:
        """Retailer serializer meta class."""

        fields = ("id", "name", "phone","pms_rate","pms_stock","ago_rate","ago_stock","dpk_rate","dpk_stock","lpg_rate","lpg_stock", "auto_shop", "supermart", "car_wash")
        geo_field = "coordinates"
        model = Retailer