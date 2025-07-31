from api.models import ShrinkInstanceModel
from api.serializers import ShrinkInstanceSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAuthenticated
from api.unique_code import generate_unique_code
from rest_framework.decorators import api_view
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
            unique_code = generate_unique_code()
            obj.shrinked_url = request.build_absolute_uri(f'/{unique_code}/')
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
@api_view(['POST'])
def redirect(request):
    pass