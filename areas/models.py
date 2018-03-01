from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    central_office = models.CharField(max_length=300)


class ServiceArea(models.Model):
    name = models.CharField(max_length=200)
    
    price = models.DecimalField(max_digits=12, decimal_places=2)

    # TODO: many-to-one
    service_type = models.CharField(max_length=25)

    provider = models.ForeignKey(
        Provider,
        # TODO: возможно лучше не удалять,
        # а назначать на предопределенного <неопределенного> поставщика
        on_delete=models.CASCADE,
    )


