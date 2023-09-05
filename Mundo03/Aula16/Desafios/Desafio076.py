'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, 
na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

print('-=-'*10, '\nCar Kay:^20\n'+'-=-'*10)

carros = ('Tucson', 30000,
          'Civic', 40000,
          'Ix35', 45000,
          'Jetta TSI', 50000,
          'Tiguan TSI', 55000,
          'I30', 35000)
for cont in range(0, len(carros)):
    if (cont % 2 == 0):
        print(carros[cont], end='')
    else:
        print(f'.......... R$ {carros[cont]:.2f}')
