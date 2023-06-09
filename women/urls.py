from django.urls import path, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'women', views.WomenViewSet, basename='women')

for url in router.urls:
    print(url)

urlpatterns = [
    path("", include(router.urls)),
    # path("womenlist/", views.WomenViewSet.as_view({'get': 'list', 'post': 'create'})),
    # path("womenlist/<int:pk>/", views.WomenViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
