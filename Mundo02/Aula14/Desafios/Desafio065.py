'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média 
entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário 
se ele quer ou não continuar a digitar valores.'''

resp='s'
soma = qaunt = cont = 0
while(resp in 'Ss'):

    n=int(input('Digite algum valor inteiro: '))
    resp=str(input('Você deseja continuar [S/N]: ')).upper().strip()[0]
    cont+=1
    soma=soma+n

    if(cont==1):
        maior = menor = n 
    else:
        if(n>maior):
            maior=n
        if(n<menor):
            menor=n

print('\nEncerrou')
print('Você digitou {} números e a média do valores foi {}'.format(cont, soma/cont))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))