import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django
django.setup()

from django.contrib.auth import get_user_model
from ranking.models import Escola, Aluno
import names
UserModel = get_user_model()

print("Populating DB...")

# Cria um usuario admin
if not UserModel.objects.filter(username='luiz').exists():
    user=UserModel.objects.create_user('luiz', password='luiz')
    user.is_superuser=True
    user.is_staff=True
    user.save()

# Cria as 3 escolas e coloca em uma lista
escola_dados, _ = Escola.objects.get_or_create(nome='Dados')
escola_tech, _ = Escola.objects.get_or_create(nome='Tecnologia')
escola_produtos, _ = Escola.objects.get_or_create(nome='Produtos')
escolas = [escola_dados, escola_tech, escola_produtos]

# Cria 15 alunos pra cada escola
for _ in range(15):
    for escola in escolas:
        created = False
        tries = 0
        while not created and tries < 5:
            _, created = Aluno.objects.get_or_create(nome=names.get_first_name(), escola=escola)
            tries += 1

print("Done!")