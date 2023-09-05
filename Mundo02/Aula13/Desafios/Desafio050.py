#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
#Se o valor digitado for ímpar, desconsidere-o.

total=0

print('-=-= Soma de números pares =-=-\n')
for cont in range(1,7):
    x=int(input('Digite o {}° valor: '.format(cont)))
    if(x%2==0):
        total=total+x

print('\nA soma dos números pares digitados é {}'.format(total))

