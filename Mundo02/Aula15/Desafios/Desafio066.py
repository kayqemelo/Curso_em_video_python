'''Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário 
digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e 
qual foi a soma entre elas (desconsiderando o flag).'''

cont = soma = 0
while(True):
    n=int(input('Digite um valor inteiro ou 999 para encerrar:\n'))

    if(n==999):
        break


    soma=soma+n
    cont+=1

print('Você digitou 999')
print(f'Você digitou {cont} números e a soma deles foi {soma}')