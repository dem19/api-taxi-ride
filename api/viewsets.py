from rest_framework.viewsets import ModelViewSet
from .serializer import CadastrarTaxista, CadastrarEmpresa
from Taxi.models import CadTaxista, EmpTaxi
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class Cad_Taxista(ModelViewSet):
    queryset = CadTaxista.objects.all()
    serializer_class = CadastrarTaxista
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class Cad_Empresa(ModelViewSet):
    queryset = EmpTaxi.objects.all()
    serializer_class = CadastrarEmpresa
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

