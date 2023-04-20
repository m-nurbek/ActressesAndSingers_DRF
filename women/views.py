from rest_framework import generics, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Women, Category
from .serializer import WomenSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly


class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

    # permission_classes = [IsAdminOrReadOnly]
    def get_permissions(self):
        if self.action == "list":
            permission_classes = [IsAdminOrReadOnly]
        elif self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        elif self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsOwnerOrReadOnly]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    # def get_queryset(self):
    #     pk = self.kwargs.get("pk")
    #     if not pk:
    #         return Women.objects.all()[:3]
    #     return Women.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def category(self, request, pk):
        c = Category.objects.get(pk=pk)
        cats = Category.objects.all()
        return Response({'categories': c.name})
        # return Response({'categories': [c.name for c in cats]})
