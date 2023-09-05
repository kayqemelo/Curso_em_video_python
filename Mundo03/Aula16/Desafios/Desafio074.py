'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, 
mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

import random

print('-=-= Tupla aleatoria =-=-\n')

aleatorio = [random.randint(0, 100) for _ in range(5)]
lista = tuple(aleatorio)

print(f'O 5 valores gerados da tupla são:\n{lista}\n')
print(f'O maior valor é {max(lista)}')
print(f'O menor valor é {min(lista)}')
