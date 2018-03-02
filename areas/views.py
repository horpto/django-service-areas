from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import serializers
#from areas.serializers import UserSerializer, GroupSerializer

from areas.models import Provider, ServiceArea


class ProviderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provider
        fields = ('name', 'email', 'phone', 'central_office')



class ProviderViewSet(viewsets.ModelViewSet):
    '''
        API Поставщиков.
    '''
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
