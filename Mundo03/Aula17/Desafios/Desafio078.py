'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre 
qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

lista = []
for cont in range(0, 5):
    lista.append(int(input(f'Digite o {cont+1}° valor: ')))

print(f'Sua lista é composta por:\n{lista}')
print(
    f'\nO maior valor da lista é {max(lista)}, e está na posição {lista.index(max(lista))}')
print(
    f'O menor valor da lista é {min(lista)}, e está na posição {lista.index(min(lista))}')
