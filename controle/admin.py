from django.contrib import admin
from datetime import date
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from simple_history.admin import SimpleHistoryAdmin
from .models import Funcionario, Setor, Controle

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display= ('nome','setor',)

@admin.register(Setor)
class SetorAdmin(SimpleHistoryAdmin):
    list_display =('nome',)

class ControleResource(resources.ModelResource):
    class Meta:
        model= Controle
        fields = ('nome__nome', 'data', 'entrada', 'saida')  # Exemplo com campos relacionados
        export_order = ('nome__nome', 'data', 'entrada', 'saida')

@admin.register(Controle)
class ControleAdmin(ImportExportModelAdmin):
    resource_class = ControleResource
    list_display =['nome','data','entrada','saida']
    list_filter = (('data',admin.DateFieldListFilter),)
    ordering= ('nome',)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Se o usuário não estiver filtrando manualmente por data,
        # mostra apenas os registros de hoje
        if 'data__gte' not in request.GET and 'data__exact' not in request.GET:
            return qs.filter(data=date.today())
        return qs
    
    

    


    
