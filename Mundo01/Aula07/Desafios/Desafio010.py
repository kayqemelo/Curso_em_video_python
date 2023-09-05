#Faça um programa que pergunte quantos reais a pessoa tem e quantos dolares ela pode comprar
#dolar a 4.78

print('--- Cambio Dolar ---')

n1=float(input('\nQuantos reias vc deseja trocar\n: '))

print('\nReais: {}'.format(n1))
print('Dolares: {:.2f}'.format(n1/4.78))