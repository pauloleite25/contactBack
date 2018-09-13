"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.db import router
from django.shortcuts import redirect
from django.templatetags.static import static
from django.urls import reverse
from django.conf.urls import include, url
from rest_framework import routers

from rest_framework_jwt.views import ObtainJSONWebToken

from rest_framework.routers import DefaultRouter

from modules.address.views import AddressViewSet
from modules.phone.views import PhoneViewSet
from modules.register_contact.views import RegisterContactViewSet
from project import settings


router = routers.DefaultRouter()

router.register(r'register', viewset=RegisterContactViewSet)
router.register(r'phone', viewset=PhoneViewSet)
router.register(r'address', viewset=AddressViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]