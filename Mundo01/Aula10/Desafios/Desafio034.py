#Pergunte o salario do funcionario e calcule seu almento 
#Se for maior que 1250, calcule um aumento de 10%
#Para inferiores ou iguais a 1250 o aumento é 15%

print('-=-= Aumento salárial =-=-')

salario=float(input('Digite o seu salário:\nR$ '))

if(salario>1250):
    aumento=float((salario*0.1)+salario)
    print('\nSeu novo salario é: R${}'.format(aumento))
else:
    aumento=float((salario*0.15)+salario)
    print('\nSeu novo salario é: R${}'.format(aumento))