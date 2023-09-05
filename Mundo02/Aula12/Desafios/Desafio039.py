#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
#se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar
#ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo
# que falta ou que passou do prazo.
from datetime import date
print('### Alistamento ###')
nascimento=int(input('\nDigite o ano do seu nascimento:\n'))

ano = date.today().year
idade=int(ano-nascimento)

if(idade==17 or idade ==18):
    print('\nEstá na hora de vc se alistar')

elif(idade<17):
    print('\nAinda faltam {} anos para você se alistar'.format(18-idade))

else:
    print('\njá se passaram {} que você se alistou ou deveria se alistar'.format(idade-18))