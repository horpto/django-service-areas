from rest_framework import routers

from areas.views import ProviderViewSet, ProvidersApiView

app_name = 'api'
router = routers.DefaultRouter()
router.register(r'providers', ProviderViewSet, base_name='provider')
router.register(r'api-provider', ProvidersApiView, base_name='api_provider')

urlpatterns = router.urls