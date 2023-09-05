# Escreva um programa que leia dois números inteiros e compare-os
# mostrando qual é maior ou se são iguais

n1=int(input('digite um valor: '))
n2=int(input('Digite outro valor: '))

if(n1>n2):
    print('\n{} é maior que {}'.format(n1,n2))
elif(n2>n1):
    print('\n{} é maior que {}'.format(n2,n1))
else:
    print('\n{} e {} são iguais'.format(n1,n2))