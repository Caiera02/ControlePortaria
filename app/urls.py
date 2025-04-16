from django.contrib import admin
from django.urls import path
from controle.views import controle_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('controle/',controle_view, name='controle_list')
]
