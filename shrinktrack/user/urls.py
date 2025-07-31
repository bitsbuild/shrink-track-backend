from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from user.views import create_user,delete_user
urlpatterns = [
    path('create/',create_user,name="create"),
    path('get-token/',obtain_auth_token,name="get-token"),
    path('delete/',delete_user,name="delete")
]