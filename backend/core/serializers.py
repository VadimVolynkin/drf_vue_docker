from rest_framework.serializers import ModelSerializer
from .models import Car

class CarSerializer(ModelSerializer):
    class Meta:
        model = Car                     # модель сериализации
        fields = "__all__"              # поля для сериализации - все или ("field_name", )