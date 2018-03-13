from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import serializers, viewsets
from rest_framework.filters import OrderingFilter


from areas.models import Provider, Service, ServiceArea



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
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_fields = '__all__'
    ordering = 'name'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ServiceViewSet(viewsets.ModelViewSet):
    '''
    API услуг
    '''
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_fields = '__all__'
    ordering = 'service_type'


class ServiceAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceArea
        fields = '__all__'



class ServiceAreaViewSet(viewsets.ModelViewSet):
    '''
    API зон обслуживания
    '''
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_fields = '__all__'
    ordering = 'name'
