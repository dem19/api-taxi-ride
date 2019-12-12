from django.db import models


class EmpTaxi(models.Model):
    nome_empresa = models.CharField(max_length=100)
    CNPJ = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_empresa

class CadTaxista(models.Model):
    Nfuncionario = models.CharField(max_length=100)
    Nempresa = models.ForeignKey(EmpTaxi, on_delete=models.CASCADE)
    bairro = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    telefone = models.CharField(max_length=16)
    RG = models.CharField(max_length=9)
    CPF = models.CharField(max_length=14)
    CNH_profissional = models.CharField(max_length=100)
    placa = models.CharField(max_length=100)
    cor_moto = models.CharField(max_length=100)

    def __str__(self):
        return f' {self.Nfuncionario}'






