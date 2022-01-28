from rest_framework import routers

from .viewsets import RetailerViewSet

router = routers.DefaultRouter()
router.register(r"retailers", RetailerViewSet)

urlpatterns = router.urls