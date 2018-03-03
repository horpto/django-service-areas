from rest_framework import viewsets, serializers, generics
from django_filters import rest_framework as filters

from areas.models import Provider, ServiceArea


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'



class ProviderViewSet(viewsets.ModelViewSet):
    '''
        API Поставщиков.
    '''
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class ProvidersApiView(generics.ListAPIView):
    '''
        API Поставщиков.
    '''
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    filter_backends = (filters.OrderingFilter,)
    filter_fields = '__all__'
    ordering_fields = '__all__'
    ordering = 'name'
