#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes

print('-=-= Triângulos =-=-')

print('\nDigite os lados do trângulos')
l1=float(input('1° lado: '))
l2=float(input('2° lado: '))
l3=float(input('3° lado: '))


if (l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 +l2):

    if(l1<0 or l2<0 or l3<0):
      print('\nValores inválidos!!!')
    elif(l1==l2==l3):
      print('\nTriângulo EQUILÁTERO')
    elif(l1!=l2!=l3):
      print('\nTriângulo ESCALENO')
    else:
      print('\nTriângulo ISÓSCELES')
else:
    print('\nValores não forman um triângulo!!!')


 