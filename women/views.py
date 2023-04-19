from rest_framework import generics

from .models import Women
from .serializer import WomenSerializer


# realizes two methods for GET and POST
class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


# GET, PUT, DELETE
class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
