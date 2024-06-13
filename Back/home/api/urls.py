from django.urls import path
from .views import BlogListAPIView, BlogDeleteAPIView, BlogDetailAPIView, BlogUpdateAPIView

urlpatterns = [
    path('list/', BlogListAPIView.as_view(), name="api-list"),
    path('delete/<pk>', BlogDeleteAPIView.as_view(), name="api-delete"),
    path('detail/<pk>', BlogDetailAPIView.as_view(), name="api-detail"),
    path('update/<pk>', BlogUpdateAPIView.as_view(), name="api-update"),
]