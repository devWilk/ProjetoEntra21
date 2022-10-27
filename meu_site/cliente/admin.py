from re import search
from django.contrib import admin
from .models import Cidade, Cliente, CPF

class AdminCliente(admin.ModelAdmin):
    list_display = ('nome','email','telefone')
    list_filter = ('nome','telefone')#preferencia deixar so um campo, pois lista fica grande
    search_fields = ('nome','email','telefone','cidade')


admin.site.register(Cidade)
admin.site.register(Cliente, AdminCliente)
admin.site.register(CPF)

                