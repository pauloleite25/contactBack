from rest_framework import serializers

from modules.address.serializer import AddressSerializer
from modules.phone.serializer import PhoneSerializer
from modules.register_contact import models


class RegisterContactSerializer (serializers.ModelSerializer):
    address_obj = AddressSerializer(read_only=True, source='address')
    phone_obj = PhoneSerializer(read_only=True, many=True, source='phone')
    class Meta:
        model = models.RegisterContact
        fields = '__all__'

