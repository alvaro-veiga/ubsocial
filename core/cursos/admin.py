from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['titulo','url', 'criado_em','atualizado_em','ativo']

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ['curso', 'nome', 'comentario', 'avaliacao', 'email', 'criado_em', 'atualizado_em','ativo']
