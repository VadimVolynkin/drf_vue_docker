from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

from . models import Car
from .serializers import CarSerializer


class MyPagination(PageNumberPagination):
    page_size = 15
    # page_size_query_param = 'page_size'
    # max_page_size = 15

class CarViewSet(ModelViewSet):
    serializer_class = CarSerializer               # how we will serialize
    queryset = Car.objects.all()                   # what we will serialize - data
    pagination_class = MyPagination                # set pagination