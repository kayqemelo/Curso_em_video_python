'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o 
jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para 
vencer.'''
import random

print('-=-= Jogo da adivinhação =-=-')
print('Adivinhe o número de 0 a 10\n')

x = random.randint(1, 10)
tentavida = int(2)

chute = int(input('1° tentativa: '))
while (chute != x):
    chute = int(input('{}° tentativa: '.format(tentavida)))
    tentavida += 1

if (chute == x):
    print('\nAcertou!')
    print('\nVocê precisou de {} tentativas para acertar'.format(tentavida-1))
