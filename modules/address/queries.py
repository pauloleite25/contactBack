from modules.address import models


def address_list():
    return models.Address.objects.all()


