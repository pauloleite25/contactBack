from django.db import models

# Create your models here.
from modules.address.models import Address
from modules.phone.models import Phone


class RegisterContact(models.Model):
    id = models.BigAutoField(
        db_column='id_register_conctact',
        primary_key=True,
        null=False,
        blank=False
    )

    name = models.CharField(
        db_column='name',
        max_length=500,
        null=False,
        blank=False
    )

    email = models.CharField(
        db_column='email',
        max_length=500,
        null=False,
        blank=True
    )

    address = models.ForeignKey(Address, models.DO_NOTHING, db_column='id_address', null=True, db_index=False,
                                related_name='id_address')

    phone = models.ManyToManyField(Phone, db_column='id_phone', null=True, blank=False)

    class Meta:
        managed = True
        db_table = 'register_contact'
        default_permissions = ('view',)
