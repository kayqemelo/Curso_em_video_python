#Solicite 4 nomes e sorteie uma ordem de apresentação
import random

print('--- Ordem apresentação ---')

n1=str(input('\nDigite o nome do 1° aluno: '))
n2=str(input('Digite o nome do 2° aluno: '))
n3=str(input('Digite o nome do 3° aluno: '))
n4=str(input('Digite o nome do 4° aluno: '))

lista = [n1, n2, n3, n4]
random.shuffle(lista)

print('\nOrdem de apresentação: ')
print(lista)
