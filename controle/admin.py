from django.contrib import admin
from datetime import date
from .models import Funcionario, Setor, Controle

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display= ('nome','setor',)

@admin.register(Setor)
class SetorAdmin(admin.ModelAdmin):
    list_display =('nome',)


@admin.register(Controle)
class ControleAdmin(admin.ModelAdmin):
    list_display =['nome','setor','data','entrada','saida']
    list_filter = (('data',admin.DateFieldListFilter),)
    ordering= ('nome',)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Se o usuário não estiver filtrando manualmente por data,
        # mostra apenas os registros de hoje
        if 'data__gte' not in request.GET and 'data__exact' not in request.GET:
            return qs.filter(data=date.today())
        return qs
    
    

    


    
