from api.models import ShrinkInstanceModel
from api.serializers import ShrinkInstanceSerializer
from rest_framework.viewsets import ModelViewSet
class ShrinkInstanceViewset(ModelViewSet):
    queryset = ShrinkInstanceModel.objects.all()
    serializer_class = ShrinkInstanceSerializer