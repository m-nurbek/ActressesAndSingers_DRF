from rest_framework import generics

from .models import Women
from .serializer import WomenSerializer


# realizes two methods for GET and POST
class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


# realizes the method PUT
class WomenAPIUpdate(generics.UpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


# realizes the method DELETE
class WomenAPIDelete(generics.DestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
