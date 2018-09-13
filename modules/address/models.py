from django.db import models

# Create your models here.


class Address(models.Model):

    id = models.BigAutoField(
        db_column='id_address',
        primary_key=True,
        null=False,
        blank=False
    )

    street = models.CharField(
        db_column='street',
        max_length=500,
        null=True,
        blank=True
    )

    number = models.CharField(
        db_column='number',
        max_length=500,
        null=True,
        blank=True
    )
    city = models.CharField(
        db_column='city',
        max_length=500,
        null=True,
        blank=True
    )

    state = models.CharField(
        db_column='state',
        max_length=500,
        null=True,
        blank=True
    )

    country = models.CharField(
        db_column='country',
        max_length=500,
        null=True,
        blank=True
    )

    class Meta:
        managed = True
        db_table = 'address'
        default_permissions = ('view',)
