from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('escola/<int:escola_id>/', views.escola, name='escola'),
    path('aluno/<int:aluno_id>/', views.aluno, name='aluno'),
    path('nota/', views.nota, name='nota'),
]
