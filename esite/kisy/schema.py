import graphene

from graphene_django.types import DjangoObjectType

from .models import Messdaten


class MessdatenType(DjangoObjectType):
    class Meta:
        model = Messdaten

class Query(graphene.AbstractType):
    pass