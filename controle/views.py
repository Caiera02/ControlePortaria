from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import date, timezone
from .models import Controle
from controle.forms import ControleForm

@login_required(login_url='/admin/')
def controle_view(request):
    control = Controle.objects.all()
    buscar = request.GET.get('search')

    if buscar:
        control = control.filter(data__icontains=buscar)
    else:
        hoje = date.today()
        control = control.filter(data=hoje)
        
    return render(
        request,
        'controle.html',
        {'controle' : control}
    )
    
@login_required(login_url='/admin/')
def registra_ponto(request):
    if request.method == 'POST':
        form = ControleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')  # Substitua pela sua URL
    else:
        form = ControleForm()

    return render(request, 'register.html', {
        'form': form,
    })
    
@login_required(login_url='/admin/')
def saida_ponto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        saida = request.POST.get('saida')
        registro = Controle.objects.filter(nome=nome, saida__isnull=True).order_by('-entrada').first()
        print(nome,saida)
        if registro:
            registro.saida = saida or timezone.now()  # usa o valor do form ou hora atual
            registro.save()
            return redirect('saida')
    else:
        new_form= ControleForm()
    
    return render(request,
                  'saida.html',
                  {'form':new_form})