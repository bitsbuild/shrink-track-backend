from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
@api_view(['POST'])
def create_user(request):
    pass
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request):
    pass