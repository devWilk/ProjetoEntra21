from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Cidade(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class CPF(models.Model):
    numero = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.numero)

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    email = models.EmailField(max_length=80)
    telefone = models.CharField(max_length=12)
    foto = models.ImageField(upload_to='fotos')
    cpf = models.OneToOneField(CPF, on_delete=models.CASCADE)
    cidade =models.ManyToManyField(Cidade)

    def __str__(self):
        return self.nome


