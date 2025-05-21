from django.contrib import admin
from django.urls import path
from django.http import HttpResponseNotFound
from controle.views import controle_view, registra_ponto, saida_ponto
from contas.views import login_view, home_view

def erro_404_view(request):
    return HttpResponseNotFound()

urlpatterns = [
    path('erro/',erro_404_view),
    path('admin/', admin.site.urls),
    path('controle/',controle_view, name='controle_list'),
    path('register/',registra_ponto, name='register'),
    path('saida/',saida_ponto, name='saida'),
    path('login/',login_view, name='login'),
    path('',home_view, name='home'),
]
