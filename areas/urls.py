from rest_framework import routers

from areas.views import ProviderViewSet, ServiceViewSet, ServiceAreaViewSet

app_name = 'api'
router = routers.DefaultRouter()
router.register('providers', ProviderViewSet, base_name='provider')
router.register('service', ServiceViewSet, base_name='service')
router.register('area', ServiceAreaViewSet, base_name='area')

urlpatterns = router.urls

