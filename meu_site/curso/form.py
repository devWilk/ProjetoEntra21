from socket import fromshare
from django import forms
from django.forms import ModelForm
from .models import Curso

class FormCurso(ModelForm):
    class Meta:
        model = Curso
        fields = ['id','nome','duracao']
        db_table = 'cursos'