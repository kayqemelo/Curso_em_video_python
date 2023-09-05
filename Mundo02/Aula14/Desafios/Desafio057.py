'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. 
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

print('-=-= Sexo =-=-')

sexo=str(input('\nDigite seu sexo[M/F]: ')).upper()
while(sexo not in 'FM'):
    sexo=str(input('Digite seu sexo[M/F]: ')).upper()

if(sexo=='F'):
    print('\nMuito Obrigada!!!')
else:
    print('\nMuito Obrigado!!!')