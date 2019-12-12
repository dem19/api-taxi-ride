from rest_framework import serializers
from Taxi.models import CadTaxista, EmpTaxi


class CadastrarTaxista(serializers.ModelSerializer):
    class Meta:
        model = CadTaxista
        fields = '__all__'

class CadastrarEmpresa(serializers.ModelSerializer):
    class Meta:
        model = EmpTaxi
        fields = '__all__'
