from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    central_office = models.CharField(max_length=300)



class ServiceType:
    # TODO: many-to-one
    service_type = models.CharField(max_length=25)
    
    
    
class ServiceArea(models.Model):
    name = models.CharField(max_length=200)
    
    price = models.DecimalField(max_digits=12, decimal_places=2)

    provider = models.ForeignKey(
        Provider,
        # TODO: возможно лучше не удалять,
        # а назначать на предопределенного <неопределенного> поставщика
        on_delete=models.CASCADE,
    )

    # TODO: индекс


class AreasServices(models.Model):
    area = models.ForeignKey(ServiceArea, on_delete=models.CASCADE)
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('area', 'service_type',)

    # TODO: индекс

