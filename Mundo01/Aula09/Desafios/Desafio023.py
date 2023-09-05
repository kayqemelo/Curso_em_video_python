#Faça um programa que leia um número de 0 9999 e mostre na tela sua unidade, dezena, centena e milhar...

print('---- Separando as casas numericas ----\n') 

x=int(input('Digite um valor entre 0 e 9999: '))

n=str(x)

print('\nMilhar: {}'.format(n[0]))
print('\nCentena: {}'.format(n[1]))
print('\nDezena: {}'.format(n[2]))
print('\nUnidade: {}'.format(n[3]))