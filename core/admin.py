from django.contrib import admin

from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_desplay = ('nome', 'preco', 'estoque','slug', 'criado', 'modificado', 'ativo')
