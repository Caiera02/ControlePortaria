from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Controle
from datetime import date

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