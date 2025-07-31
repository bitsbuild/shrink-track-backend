from rest_framework.routers import DefaultRouter
from api.views import ShrinkInstanceViewset
router = DefaultRouter()
router.register(r'shrink',ShrinkInstanceViewset,basename='shrink')
urlpatterns = router.urls
