from django.urls import path, include

from .views import (
    ListCreateItineraryAPIView,
    UpdateDestroyItineraryAPIView,
)


urlpatterns = [
    path(
        "itineraries/",
        ListCreateItineraryAPIView.as_view()),
    path(
        "itineraries/<pk>/",
        UpdateDestroyItineraryAPIView.as_view()),
]
