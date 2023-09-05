#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, 
#mostre os 10 primeiros termos dessa progressão.

print('-=-= Progressão aritimética =-=-')
pro=int(input('\nDigite o 1° termo dessa progressão: '))
raz=int(input('Digite a razão dessa progressão: '))
quantidade=int(10*raz+pro)
print('')

for cont in range(pro,quantidade,raz):
    print(cont, end=' ')