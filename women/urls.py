from django.urls import path, include
from . import views

urlpatterns = [
    path("api/v1/womenlist/", views.WomenAPIView.as_view()),
    path("api/v1/womenlist/<int:pk/>", views.WomenAPIView.as_view()),
]
