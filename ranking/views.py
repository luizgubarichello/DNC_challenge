from django.shortcuts import render, redirect
from .models import Escola, Aluno, Nota

def index(request):
    # Uma view para a página inicial da aplicação
    escolas = Escola.objects.all()
    alunos = Aluno.objects.all()
    podio = Aluno.objects.order_by('-pontuacao')[:3]
    return render(request, 'ranking/index.html', {'escolas': escolas, 'alunos': alunos, 'podio': podio})

def escola(request, escola_id):
    # Uma view para a página de uma escola específica
    escola = Escola.objects.get(pk=escola_id)
    alunos = Aluno.objects.filter(escola=escola).order_by('-pontuacao')[:10]
    return render(request, 'ranking/escola.html', {'escola': escola, 'alunos': alunos})

def aluno(request, aluno_id):
    # Uma view para a página de um aluno específico
    aluno = Aluno.objects.get(pk=aluno_id)
    notas = Nota.objects.filter(aluno=aluno)
    return render(request, 'ranking/aluno.html', {'aluno': aluno, 'notas': notas})

def nota(request):
    # Uma view para a página de inserção de nota
    if request.method == 'POST':
        tipo = request.POST['tipo']
        valor = int(request.POST['valor'])
        aluno_id = request.POST['aluno']

        aluno = Aluno.objects.get(pk=aluno_id)
        nota, _ = Nota.objects.get_or_create(tipo=tipo, aluno=aluno)
        nota.valor = valor
        nota.save()

        notas = Nota.objects.filter(aluno=aluno)
        escola = Escola.objects.get(pk=aluno.escola.pk)
        pesos = {
            'T': escola.peso_tarefa,
            'D': escola.peso_desafio,
            'P': escola.peso_projeto,
        }
        pontuacao = 0
        for nota in notas:
            pontuacao += nota.valor * pesos[nota.tipo]
        pontuacao /= sum(pesos.values())
        aluno.pontuacao = pontuacao
        aluno.save()

        return redirect('index')
    
    if request.method == 'GET':
        alunos = Aluno.objects.all()
        return render(request, 'ranking/nota.html', {'alunos': alunos})