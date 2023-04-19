from django.urls import path, include
from . import views

urlpatterns = [
    path("api/v1/womenlist/", views.WomenAPIList.as_view()),
    path("api/v1/womendetail/<int:pk>/", views.WomenAPIDetailView.as_view()),
]
