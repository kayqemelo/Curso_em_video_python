'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar [ 2 ] multiplicar [ 3 ] maior [ 4 ] novos números [ 5 ] sair do programa'''

x=int(0)

n1=float(input('Digite o 1° valor: '))
n2=float(input('Digite o 2° valor: '))

while x !=5:

    print('\n[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')

    x=int(input('\nOpção: '))

    if(x==1):
        print('\n{} + {} = {}'.format(n1,n2,n1+n2))
    elif(x==2):
        print('\n{} x {} = {}'.format(n1,n2,n1*n2))
    elif(x==3):
        if(n1>n2):
            print('\n{} é maior que {}'.format(n1,n2))
        if(n1<n2):
            print('\n{} é maior que {}'.format(n2,n1))
        else:
            print('\n{} e {} são valores iguais'.format(n1, n2))
    elif(x==4):
        n1=float(input('Digite o 1° valor: '))
        n2=float(input('Digite o 2° valor: '))
    elif(x==5):
        print('\nOpção sair')
    else:
        print('Opção inválida :(')    

print('Saindo do programa...')
    
        