from random import choices
from django_filters.rest_framework import filterset, filters
from modules.phone import models


class PhoneFilter(filterset.FilterSet):
    number = filters.CharFilter()

    class Meta:
        model = models.Phone
        fields = ['number']