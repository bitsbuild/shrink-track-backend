from rest_framework.serializers import ModelSerializer
from api.models import UrlConvertInstance
class ConvertInstanceSerializer(ModelSerializer):
    class Meta:
        model = UrlConvertInstance
        fields = '__all__'