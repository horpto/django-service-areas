from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers, viewsets
from rest_framework.filters import OrderingFilter

from areas.models import Provider


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'


class ProviderViewSet(viewsets.ModelViewSet):
    """
    API Поставщиков.
    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = '__all__'


class ProvidersApiView(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    filter_fields = '__all__'
    ordering = 'name'
