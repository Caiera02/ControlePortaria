from django.contrib import admin
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
    
    

    


    
