from rest_framework import routers

from areas.views import ProviderViewSet

app_name = 'api'
router = routers.DefaultRouter()
router.register('providers', ProviderViewSet, base_name='provider')

urlpatterns = router.urls

