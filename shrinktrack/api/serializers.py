from rest_framework.serializers import ModelSerializer
from api.models import ShrinkInstanceModel
class ShrinkInstanceSerializer(ModelSerializer):
    class Meta:
        model = ShrinkInstanceModel
        fields = [
            'original_url',
        ]
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)