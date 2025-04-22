from django.contrib import admin
from django.urls import path
from controle.views import controle_view, registra_ponto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('controle/',controle_view, name='controle_list'),
    path('register/',registra_ponto, name='register'),
]
