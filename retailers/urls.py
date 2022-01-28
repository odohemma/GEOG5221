from django.urls import path

from retailers.views import RetailersMapView



urlpatterns = [
    path('', RetailersMapView.as_view(), name='home'),
]