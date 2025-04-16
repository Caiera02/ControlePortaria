from django.db import models


class Setor(models.Model):
    nome = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name =' Setore'
        
class Funcionario(models.Model):
    nome= models.CharField(max_length=60)
    setor= models.ForeignKey(Setor, on_delete=models.PROTECT,
                              related_name='setor', verbose_name='departamento')
    
    def __str__(self):
        return self.nome
    
    class Meta:
        ordering= ['nome']
        verbose_name = 'Cooperado'


class Controle(models.Model):
    nome= models.ForeignKey(Funcionario, on_delete=models.PROTECT,
                             related_name='funcionario', verbose_name='Nome')
    setor= models.ForeignKey(Setor, on_delete=models.PROTECT,
                              related_name='funcionario', verbose_name='departamento')
    data= models.DateField(auto_now_add=True)
    entrada= models.TimeField( verbose_name= 'Entrada')
    saida= models.TimeField( verbose_name= 'saida',blank=True, null=True)

    class Meta:
        ordering= ['nome']
        unique_together = ('nome', 'data')