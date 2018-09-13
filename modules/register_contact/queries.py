from modules.register_contact import models


def register_contact_list():
    return models.RegisterContact.objects.all()


