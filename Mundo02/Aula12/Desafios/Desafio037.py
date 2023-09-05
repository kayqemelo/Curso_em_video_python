# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher 
# qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

print('-= Conversão de bases =-')
x=int(input('\nDigite o número que deseja converter:\n')) 


print('\n[1] Binário')
print('[2] Octal')
print('[3] Hexadecimal')
opção=int(input('Converter para: '))

if(opção==1):
    print('{} convertido para binario é igual a {}'.format(x, bin(x)[2:]))

elif(opção==2):
    print('{} convertido para octal é igual a {}'.format(x, oct(x)[2:]))

elif(opção==3):
    print('{} convertido para Hexadecimal é igual a {}'.format(x, hex(x)[2:]))

else:
    print('Opção inválida')


