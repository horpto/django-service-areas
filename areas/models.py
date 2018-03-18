from django.db import models
from django.contrib.gis.db import models as gis_models


class Provider(models.Model):
    '''
    Поставщик услуг в различных 
    '''
    name = models.CharField(max_length=200, unique=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    central_office = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Service(models.Model):
    '''
    Услуга, предоставляемая поставщиками
    '''
    service_type = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.service_type


class ServiceArea(models.Model):
    '''
    "Зона обслуживания" для служб эксплуатации
    '''
    name = models.CharField(max_length=200)    
    price = models.DecimalField(max_digits=12, decimal_places=2)
    polygon = gis_models.PolygonField()

    provider = models.ForeignKey(
        Provider,
        # TODO: возможно лучше не удалять,
        # а назначать на предопределенного <неопределенного> поставщика
        on_delete=models.CASCADE,
    )
    services = models.ManyToManyField(Service, blank=True)
    # TODO: индекс

    def __str__(self):
        return self.name
