#Pergunte um número e analise se ele é impar ou par

print('Impar ou par?')

numero=int(input('\nDigite um número: '))

if(numero%2==0):
    print('{} é par!'.format(numero))
else:
    print('{} é impar!'.format(numero))