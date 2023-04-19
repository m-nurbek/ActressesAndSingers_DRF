from django.urls import path, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'women', views.WomenViewSet)

for url in router.urls:
    print(url)

urlpatterns = [
    path("api/v1/", include(router.urls)),
    # path("api/v1/womenlist/", views.WomenViewSet.as_view({'get': 'list', 'post': 'create'})),
    # path("api/v1/womenlist/<int:pk>/", views.WomenViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
