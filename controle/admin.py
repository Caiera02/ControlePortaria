from django.contrib import admin
from .models import Funcionario, Setor, Controle
from datetime import datetime

# Register your models here.

from django.contrib import admin
from .models import Controle
from datetime import datetime

class DataFiltro(admin.SimpleListFilter):
    title = 'Data'  # Nome do filtro que vai aparecer
    parameter_name = 'data'  # Nome do parâmetro na URL

    def lookups(self, request, model_admin):
        return []  # Nenhuma opção fixa, vamos usar input manual

    def queryset(self, request, queryset):
        data_str = request.GET.get(self.parameter_name)
        if data_str:
            try:
                # Tenta converter string para data (espera no formato YYYY-MM-DD)
                data = datetime.strptime(data_str, '%Y-%m-%d').date()
                return queryset.filter(data=data)
            except ValueError:
                return queryset.none()
        return queryset



@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display= ('nome','setor',)

@admin.register(Setor)
class SetorAdmin(admin.ModelAdmin):
    list_display =('nome',)


@admin.register(Controle)
class ControleAdmin(admin.ModelAdmin):
    list_display =['nome','setor','data','entrada']
    list_filter = (DataFiltro,)
    # list_filter = (('data',admin.DateFieldListFilter),)
    
    

    


    
