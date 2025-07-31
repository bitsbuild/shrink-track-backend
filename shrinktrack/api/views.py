from api.models import ShrinkInstanceModel
from api.serializers import ShrinkInstanceSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAuthenticated
class ShrinkInstanceViewset(ModelViewSet):
    queryset = ShrinkInstanceModel.objects.all()
    serializer_class = ShrinkInstanceSerializer
    permission_classes = [IsAuthenticated]
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            obj = ShrinkInstanceModel.objects.get(original_url=request.data['original_url'])
            obj.shrinked_url = None
            obj.save()
            return Response(
                {
                    "Status":"URL Shrinked Successfuly"
                },status=HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {
                    "Status":"Shrink Process Failed",
                    "Error":str(e)
                },status=HTTP_400_BAD_REQUEST
            )