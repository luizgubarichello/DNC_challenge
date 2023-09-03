from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls), # Uma rota para a interface administrativa do Django
    path('', include('ranking.urls')), # Uma rota que inclui as rotas da aplicação ranking
]
