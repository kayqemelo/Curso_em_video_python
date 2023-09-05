#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
print('-=-= Números primos =-=-')
x=int(input('Digite um valor: '))
y=0

for cont in range(1,x+1):
    if(x%cont==0):
        y+=1

if(y==2):
    print('\n{} é um número primo'.format(x))
else:
    print('\n{} não é um número primo'.format(x))
