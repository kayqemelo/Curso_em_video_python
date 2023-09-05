'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até 
vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

print('-=-= Número por extenso =-=-')

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete','oito','nove', 'des', 'onze', 
        'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while(True):

    x=int(input('\nDigite um valor de 0 a 20: '))
    if(x >=0 and x <=20):
        print(f'{x} = {numeros[x]}\n')
        y=str(input('Deseja continuar[S/N]: ')).strip().upper()[0]
        if(y == 'N'):
            break
    else:
        print('Tente novamente')

print('FIM!')