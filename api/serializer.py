from rest_framework import serializers
from Taxi.models import CadTaxista


class CadastrarTaxista(serializers.ModelSerializer):
    class Meta:
        model = CadTaxista
        fields = '__all__'

