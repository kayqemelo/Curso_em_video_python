#solicite o nome de 4 alunos e faça um sorteio
import random

print('      --- Soretio ---')
n1=str(input('\nDigite o nome do 1° aluno: '))
n2=str(input('Digite o nome do 2° aluno: '))
n3=str(input('Digite o nome do 3° aluno: '))
n4=str(input('Digite o nome do 4° aluno: '))

lista = [n1, n2, n3, n4]

print('\nNome sorteado: ')
print(random.choice(lista))
