from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import date
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
def registra_ponto(request, pk=None):
    if request.method == 'POST':
        form = ControleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('controle_list')
    else:
        form = ControleForm()

    return render(request, 'register.html', {
        'form': form,
    })