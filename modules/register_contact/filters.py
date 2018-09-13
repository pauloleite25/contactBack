from random import choices
from django_filters.rest_framework import filterset, filters
from modules.register_contact import models


class RegisterContactFilter(filterset.FilterSet):
    description = filters.CharFilter()

    class Meta:
        model = models.RegisterContact
        fields = ['description']