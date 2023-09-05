#Faça um codigo que pessa o salário de um FuncionÁrio e mostre seu novo salário. com 15% de aumento.

print('--- novo salário ---')
n1=float(input('\nDigite seu salário: '))
desconto=float((n1*15)/100)

print('Seu novo salário: {:.2f}' .format(n1+desconto))