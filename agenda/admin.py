from django.contrib import admin
from .models import Servico, Espera

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao','preco')

@admin.register(Espera)
class EsperaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'servico', 'data', 'hora', 'status')
    list_filter = ('status', 'data', 'servico')
