#Verique se 3 segmentos formam um triangulo

print('-=-= Triângulos =-=-\n')

n1=float(input('Digite o 1° segmento: '))
n2=float(input('Digite o 2° segmento: '))
n3=float(input('Digite o 3° segmento: '))
print(' ')


if(n1>=n2 and n1>=n3):
    if(n2+n3>n1):
        print('Forma triangulo')
    else:
        print('Não forma triangulo')
elif(n2>=n1 and n2>=n3):
    if(n1+n3>n2):
        print('Forma triangulo')
    else:
        print('Não forma triangulo')
elif(n3>=n1 and n3>=n2):
    if(n1+n2>n3):
        print('Forma triangulo')
    else:
        print('Não forma triangulo')