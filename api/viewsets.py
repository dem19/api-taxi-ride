from rest_framework.viewsets import ModelViewSet
from .serializer import CadastrarTaxista
from Taxi.models import CadTaxista
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated,DjangoModelPermissionsOrAnonReadOnly
from django.shortcuts import get_object_or_404

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class ListagemTaxista(ModelViewSet):
    queryset = CadTaxista.objects.all()
    serializer_class = CadastrarTaxista
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

