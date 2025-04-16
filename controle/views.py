from django.shortcuts import render
from .models import Controle

def controle_view(request):
    control = Controle.objects.all()
    buscar =request.GET.get('search')

    if buscar:
        control = control.filter(data__icontains=buscar)

    return render(
        request,
        'controle.html',
        {'controle' : control}
    )