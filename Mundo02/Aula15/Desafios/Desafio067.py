'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo
 usuário. O programa será interrompido quando o número solicitado for negativo.'''

print('-=-= TABUADA =-=-')




while(True):
    cont=0
    print('\nDigite algum valor negativo para sair')
    x=int(input('Digite o valor da tabuada que dejesa descobrir: '))
    if(x<0):
        break

    while(cont!=11):
        print(f'{x} x {cont} = {x*cont}')
        cont+=1

print('\nVocê saiu do programa!!!')