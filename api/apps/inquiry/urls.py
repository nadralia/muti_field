from django.urls import path, include

from .views import (
    ListCreateInquiryView,
    UpdateDestroyInquiryView,
)


urlpatterns = [
    path(
        "inquiries/",
        ListCreateInquiryView.as_view()),
    path(
        "inquiries/<pk>/",
        UpdateDestroyInquiryView.as_view()),
]
