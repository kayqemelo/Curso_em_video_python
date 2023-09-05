'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o 
usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram 
digitados e qual foi a soma entre eles'''

cont=0
n=int(0)
soma=int(0)

print('Digite um valor inteiro diferente de 999 ou não...\n')
while(n!=999):

    n=int(input())
    soma=soma+n
    cont+=1


print('\nInfelizmente você digitou 999...')
print('Foram digitados {} número(s)\nJuntos eles somaram {}'.format(cont-1, soma-999))