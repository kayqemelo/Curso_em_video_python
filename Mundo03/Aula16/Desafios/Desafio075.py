'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. 
No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.'''

a = int(input('1° valor: '))
b = int(input('2° valor: '))
c = int(input('3° valor: '))
d = int(input('4° valor: '))
r = 0
lista = (a, b, c, d)
print(f'\n{lista}')

print(f'\nO número 9 aparece {lista.count(9)} vezes')

if (3 in lista):
    print(f'O primeiro número 3 está na posição {lista.index(3)+1}')
else:
    print('Não existe o número 3')


for cont in lista:
    if (cont % 2 == 0):
        r += 1
print(f'Na lista tem {r} números pares')
