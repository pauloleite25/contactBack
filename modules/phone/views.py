from django.db.models import Count
from django.db.models.functions import Extract
from rest_framework import viewsets, status
from rest_framework.decorators import list_route
from rest_framework.response import Response

from modules.phone import queries
from modules.phone.filters import PhoneFilter
from modules.phone.models import Phone
from modules.phone.serializer import PhoneSerializer


class PhoneViewSet(viewsets.ModelViewSet):
    queryset = queries.phone_list()
    serializer_class = PhoneSerializer
    filter_class = PhoneFilter

    def create(self, request, *args, **kwargs):
        data = request.data
        return_data = []
        for phone in data:
            new_phone = Phone(number=phone.get('number'), type=phone.get('type'))
            new_phone.save()
            return_data.append(new_phone)
        result_serializer = PhoneSerializer(instance=return_data, many=True, context={'request': request})
        return Response(result_serializer.data, status=status.HTTP_201_CREATED)

    @list_route(methods=['get'])
    def get_phone_type(self, request):
        query = Phone.objects.annotate().values('type').annotate(experiments=Count('type'))
        return Response(query)
