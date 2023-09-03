from django.test import TestCase
from .models import Escola, Aluno, Nota

class ModelTestCase(TestCase):
    # Uma classe de teste para os modelos da aplicação
    def setUp(self):
        self.escola = Escola.objects.create(nome='Escola de Dados')
        self.aluno = Aluno.objects.create(nome='Alice', escola=self.escola)
        self.nota = Nota.objects.create(tipo='T', valor=80, aluno=self.aluno)

    def test_escola_str(self):
        # Um método de teste para verificar a representação em string do modelo Escola
        self.assertEqual(str(self.escola), 'Escola de Dados')

    def test_aluno_str(self):
        # Um método de teste para verificar a representação em string do modelo Aluno
        self.assertEqual(str(self.aluno), 'Alice')

    def test_nota_str(self):
        # Um método de teste para verificar a representação em string do modelo Nota
        self.assertEqual(str(self.nota), 'T: 80')

class ViewTestCase(TestCase):
    # Uma classe de teste para as views da aplicação
    def setUp(self):
        self.escola = Escola.objects.create(nome='Escola de Tecnologia')
        self.aluno = Aluno.objects.create(nome='Bob', escola=self.escola, pontuacao=100)
        self.nota = Nota.objects.create(tipo='P', valor=100, aluno=self.aluno)

    def test_index_view(self):
        # Um método de teste para verificar a view index
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Ranking de Alunos')
        self.assertQuerysetEqual(map(repr, response.context['escolas']), ['<Escola: Escola de Tecnologia>'])
        self.assertQuerysetEqual(map(repr, response.context['podio']), ['<Aluno: Bob>'])

    def test_escola_view(self):
        # Um método de teste para verificar a view escola
        response = self.client.get(f'/escola/{self.escola.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Escola de Tecnologia')
        self.assertQuerysetEqual(map(repr, response.context['alunos']), ['<Aluno: Bob>'])

    def test_aluno_view(self):
        # Um método de teste para verificar a view aluno
        response = self.client.get(f'/aluno/{self.aluno.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Bob')
        self.assertContains(response, 'Escola de Tecnologia')
        self.assertQuerysetEqual(map(repr, response.context['notas']), ['<Nota: P: 100>'])

    def test_nota_view(self):
        # Um método de teste para verificar a view nota
        response = self.client.get('/nota/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Inserir Nota')
        response = self.client.post('/nota/', {'tipo': 'D', 'valor': 80, 'aluno': self.aluno.id})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        self.assertEqual(Nota.objects.count(), 2)
        self.assertEqual(Aluno.objects.get(pk=self.aluno.id).pontuacao, 60)
