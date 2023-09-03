from django.db import models

class Escola(models.Model):
    # Um modelo para representar uma escola
    nome = models.CharField(max_length=100)
    peso_tarefa = models.IntegerField(default=1)
    peso_desafio = models.IntegerField(default=1)
    peso_projeto = models.IntegerField(default=1)
    def __str__(self):
        return self.nome

class Aluno(models.Model):
    # Um modelo para representar um aluno
    nome = models.CharField(max_length=100)
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE)
    pontuacao = models.IntegerField(default=0)
    def __str__(self):
        return self.nome

class Nota(models.Model):
    # Um modelo para representar as notas de cada aluno
    TIPOS = (
        ('T', 'Tarefa'),
        ('D', 'Desafio'),
        ('P', 'Projeto'),
    )
    tipo = models.CharField(max_length=1, choices=TIPOS)
    valor = models.IntegerField(default=0)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.tipo}: {self.valor}'
