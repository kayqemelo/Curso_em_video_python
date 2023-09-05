#Faça um programa que leia um número de 0 9999 e mostre na tela sua unidade, dezena, centena e milhar...


print('---- Separando as casas numericas ----\n') 

x=int(input('Digite um valor entre 0 e 9999: '))

print('\nMilhar: {}'.format((x//1000)))

print('\nCentena: {}'.format((x//100%10)))

print('\nDezena: {}'.format((x//10%10)))

print('\nUnidade: {}'.format((x//1%10)))