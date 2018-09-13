from rest_framework import viewsets

from modules.address import queries
from modules.address.filters import AddressFilter
from modules.address.serializer import AddressSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = queries.address_list()
    serializer_class = AddressSerializer
    filter_class = AddressFilter
