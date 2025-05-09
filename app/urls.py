from django.contrib import admin
from django.urls import path
from controle.views import controle_view, registra_ponto, saida_ponto
from contas.views import login_view, home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('controle/',controle_view, name='controle_list'),
    path('register/',registra_ponto, name='register'),
    path('saida/',saida_ponto, name='saida'),
    path('login/',login_view, name='login'),
    path('home/',home_view, name='home'),
]
