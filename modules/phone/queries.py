from modules.phone import models


def phone_list():
    return models.Phone.objects.all()


