#Pergunte 3 valores e retorne o maior e o menor 

n1=float(input('Digite o 1° valor: '))
n2=float(input('Digite o 2° valor: '))
n3=float(input('Digite o 3° valor: '))

if(n1>n2 and n2>n3):
    print('1maior: {}, menor: {}'.format(n1,n3))
elif(n1>n2 and n2<n3):
    print('1maior: {}, menor: {}'.format(n1,n2))

elif(n2>n1 and n1>n3):
    print('21maior: {}, menor: {}'.format(n2,n3))
elif(n2>n1 and n1>n3):
    print('22maior: {}, menor: {}'.format(n2,n1))

elif(n3>n2 and n2>n1):
    print('3maior: {}, menor: {}'.format(n3,n1))
elif(n3>n2 and n2<n1):
    print('3maior: {}, menor: {}'.format(n3,n2))


       
         