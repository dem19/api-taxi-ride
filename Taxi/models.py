from django.db import models

class CadTaxista(models.Model):
    Nfuncionario = models.CharField(max_length=100)
    Nempresa = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)



    def __str__(self):
        return self.Nempresa



