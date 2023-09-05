#Ler um número real como por exemplo 6.784 e mostarr sua porção inteira, por exemplo 6
import math

x=float(input('Digite um número real: '))


print('\nO valor inteiro de {} é {}'.format(x, math.trunc(x)))