from rest_framework import serializers
from modules.phone import models


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Phone
        fields = '__all__'

