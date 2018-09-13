from random import choices
from django_filters.rest_framework import filterset, filters
from modules.address import models


class AddressFilter(filterset.FilterSet):
    description = filters.CharFilter()

    class Meta:
        model = models.Address
        fields = ['description']