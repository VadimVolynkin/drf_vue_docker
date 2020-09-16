from rest_framework.viewsets import ModelViewSet

from . models import Car
from .serializers import CarSerializer


class CarViewSet(ModelViewSet):
    serializer_class = CarSerializer               # как сереиализуем
    queryset = Car.objects.all()                   # что сереализуем
