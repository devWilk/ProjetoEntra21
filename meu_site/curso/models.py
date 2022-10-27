import re
from django.db import models

# Create your models here.

class Curso(models.Model):
    nome = models.CharField(max_length= 50)
    duracao = models.IntegerField()

    class Meta:
        db_table = 'Cursos'

    def __str__(self):
        return self.nome