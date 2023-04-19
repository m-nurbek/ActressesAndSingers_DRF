from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Women, Category
from .serializer import WomenSerializer


class WomenViewSet(viewsets.ModelViewSet):
    # queryset = Women.objects.all()
    serializer_class = WomenSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return Women.objects.all()[:3]

        return Women.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def category(self, request, pk):
        c = Category.objects.get(pk=pk)
        cats = Category.objects.all()
        return Response({'categories': c.name})
        # return Response({'categories': [c.name for c in cats]})

