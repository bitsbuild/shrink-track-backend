from rest_framework.serializers import ModelSerializer
from api.models import ShrinkInstanceModel
class ShrinkInstanceSerializer(ModelSerializer):
    class Meta:
        model = ShrinkInstanceModel
        fields = '__all__'