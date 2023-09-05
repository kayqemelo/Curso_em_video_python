#Pergunte os valores dos catetos e descubra a area da triangulo retangulo
import math

print('--- Pitágoras ---')
print('\nDigite o tamanho do:')
co=float(input('cateto oposto: '))
ca=float(input('cateto adjacente: '))

hi=float(math.sqrt((math.pow(co, 2))+(math.pow(ca, 2))))

print('A area desse triangulo retanhulo é {:.2f}'.format(hi))
