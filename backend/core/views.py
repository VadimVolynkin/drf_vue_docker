from rest_framework.viewsets import ModelViewSet

from . models import Car
from .serializers import CarSerializer


class CarViewSet(ModelViewSet):
    serializer_class = CarSerializer               # how we will serialize
    queryset = Car.objects.all()                   # what we will serialize - data
