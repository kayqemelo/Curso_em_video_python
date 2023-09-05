#Crie um programa que faça o computador jogar Jokenpô com você.
import random

print('\nVamos jogar pedra papel e tesoura')
print('[1] Sim | [2] Não')
x=int(input(''))

if(x==1):

    print('\nEscolha sua jogada')
    print('[1] PEDRA')
    print('[2] PAPEL')
    print('[3] TESOURA')
    jogada=int(input('Opção: '))

    jogadam = random.randint(1,3)

    if(jogada==1):
        if(jogada==1 and jogadam==1):
            print('\nVocê: PEDRA\nMaquina: PEDRA\n\nEmpate')
        elif(jogada==1 and jogadam==2):
            print('\nVocê: PEDRA\nMaquina: PAPEL\n\nDerrota')
        elif(jogada==1 and jogada==3):
            print('\nVocê: PEDRA\nMaquina: TESOURA\n\nVitória')

    elif(jogada==2):
        if(jogada==2 and jogadam==1):
            print('\nVocê: PAPEL\nMaquina: PEDRA\n\nVitória')
        elif(jogada==2 and jogadam==2):
            print('\nVocê: PAPEL\nMaquina: PAPEL\n\nEmpate')
        elif(jogada==2 and jogadam==3):
            print('\nVocê: PAPEL\nMaquina: TESOURA\n\nDerrota')
    
    elif(jogada==3):
        if(jogada==3 and jogadam==1):
            print('\nVocê: TESOURA\nMaquina: PEDRA\n\nDerrota')
        elif(jogada==3 and jogadam==2):
            print('\nVocê: TESOURA\nMaquina: PAPEL\n\nVitória')
        elif(jogada==3 and jogadam==3):
            print('\nVocê: TESOURA\nMaquina: TESOURA\n\nEmpate')

    else:
        print('\nOpção inválida!!!')
    
elif(x==2):
    print('Ok, adeus')
else:
    print('Opção inválida')
