from api.models import ShrinkInstanceModel
from api.serializers import ShrinkInstanceSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAuthenticated
from api.unique_code import generate_unique_code
from rest_framework.pagination import PageNumberPagination
class ShrinkInstanceViewset(ModelViewSet):
    queryset = ShrinkInstanceModel.objects.all()
    serializer_class = ShrinkInstanceSerializer
    permission_classes = [IsAuthenticated]
    pagination_class =  PageNumberPagination
    def create(self, request, *args, **kwargs):
        try:
            unique_code = generate_unique_code()
            shrinked_url = request.build_absolute_uri(f'/{unique_code}/')
            data = {
                "original_url":request.data['original_url'],
                "shrinked_url":shrinked_url
            }
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(
                {
                "Status":"Shrinked URL Generated Successfully",
                "Shrinked URL":shrinked_url
                },status=HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "Status":"Shrink Process Failed",
                    "Error":str(e)
                },status=HTTP_400_BAD_REQUEST
            )
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)