from django.shortcuts import get_object_or_404,redirect
from api.models import ShrinkInstanceModel
def redirect_view(request,code):
    instance = get_object_or_404(ShrinkInstanceModel,shrinked_url=f'https://shrink-track.onrender.com/{code}/')
    return redirect(instance.original_url)