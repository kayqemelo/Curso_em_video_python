'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerrará quando ele disser que quer mostrar 0 termos.'''

print('-=-= Super progressão =-=-\n')
ptermo=float(input('Digite o 1° termo da progressão: '))
razao=float(input('Digite a razão da progressão: '))
termos=int(input('Digite quantos termos quer ver: '))
print('')
cont=1


if(termos>0):

    while(cont<=termos):

        print('{}° termo: {}'.format(cont, ptermo))
        ptermo+=razao

        cont+=1
else:
    print('Quantidade de termos inválido!!!')




