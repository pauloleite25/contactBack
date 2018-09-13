from django.db import models

# Create your models here.


class Phone(models.Model):
    id = models.BigAutoField(
        db_column='id_phone',
        primary_key=True,
        null=False,
        blank=False
    )

    number = models.CharField(
        db_column='number',
        max_length=500,
        null=False,
        blank=False
    )

    type = models.IntegerField(
        db_column='type',
        null=False,
        blank=False
    )

    class Meta:
        managed = True
        db_table = 'phone'
        default_permissions = ('view',)
