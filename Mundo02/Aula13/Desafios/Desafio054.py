#Crie um programa que leia o ano de nascimento de sete pessoas. No final, 
#mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
print('-=-= Maioridade =-=-')
print('\nVamos captar a idade de 7 pessoas')

pessoas=0
for cont in range(1,8):
    anonasc=int(input('Digite o ano de nascimento da {}° pessoa: '.format(cont)))
    ano = date.today().year
    idades=(ano-anonasc)
    if(idades>=18):
        pessoas=pessoas+1


if(pessoas==1):
   print('\nApenas {} pessoa é maior de idade'.format(pessoas))

elif(pessoas>1):
    print('\n{} pessoas são maiores de idade'.format(pessoas))

