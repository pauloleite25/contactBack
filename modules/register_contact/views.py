# Create your views here.
from rest_framework import viewsets

from modules.register_contact import queries
from modules.register_contact.filters import RegisterContactFilter
from modules.register_contact.serializer import RegisterContactSerializer


class RegisterContactViewSet(viewsets.ModelViewSet):
    queryset = queries.register_contact_list()
    serializer_class = RegisterContactSerializer
    filter_class = RegisterContactFilter