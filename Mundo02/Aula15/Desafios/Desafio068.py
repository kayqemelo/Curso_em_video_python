'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o 
jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
import random
print('-=-= Par ou Ímpar =-=-')
cont=0

while(True):
    n = random.randint(0,5)
   
    escolha=str(input('\nVocê deseja jogar Par(P) ou Ímpar(I): ')).strip().upper()[0]
    jogada=int(input('Digite a sua jogada (0 a 5): '))

    if(jogada<=5 and jogada>=0):

        if(escolha=='P'):
            if((jogada+n)%2==0):
                print(f'\nO robo jogou {n} e você {jogada}. Vitoria!')
                cont+=1
            else:
                print(f'\nO robo jogou {n} e você {jogada}. Derrota!')
                break
        elif(escolha=='I'):
            if((jogada+n)%2==1):
                print(f'\nO robo jogou {n} e você {jogada}. Vitoria!')
                cont+=1
            else:
                print(f'\nO robo jogou {n} e você {jogada}. Derrota!')
                break
        else:
            print('\nOpção inválida')
    else:
        print('\nOpção inválida')  

print(f'\nVocê perdeu, mas obteve {cont} vitória(s)')