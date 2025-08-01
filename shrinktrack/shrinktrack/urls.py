from django.contrib import admin
from django.urls import path,include
from shrinktrack.redirect import redirect_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('user.urls')),
    path('api/',include('api.urls')),
    path('<str:code>/',redirect_view,name='redirect')
]