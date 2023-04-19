from django.urls import path, include
from . import views

urlpatterns = [
    path("api/v1/womenlist/", views.WomenAPIList.as_view()),
    path("api/v1/womenlist/<int:pk>/", views.WomenAPIUpdate.as_view()),
    path("api/v1/womenlist/d/<int:pk>/", views.WomenAPIDelete.as_view()),
]
