from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from .permission import IsOwnerOrReadOnly
from rest_framework.filters import SearchFilter

class CarViewSets(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnl]


class BetVewSets(viewsets.ModelViewSet):
    queryset = Bet.objects.all()
    serializer_class = BetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]