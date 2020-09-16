from rest_framework.serializers import ModelSerializer
from .models import Car

class CarSerializer(ModelSerializer):
    class Meta:
        model = Car                     # model
        fields = "__all__"              # all fields or ("field_name1", "field_name2")