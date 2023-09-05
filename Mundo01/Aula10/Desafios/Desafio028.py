#Crie um programa onde a maquina "pensa" em um n° de 0 a 5 e tente adivinhar 
import random

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Vou pensar em número de 0 a 5')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

sorteio = random.randint(0,5)

numero=int(input('\nQual número você acha que eu estou pensanso:\n'))

if(numero==sorteio):
    print('\nParabens você acertou :) o número é {}'.format(numero))
else:
    print('\nQue pena você errou :( o número era {}!'.format(sorteio))
