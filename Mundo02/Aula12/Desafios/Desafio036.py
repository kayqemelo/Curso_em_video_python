# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do compradore em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado"

print('-=-= Empréstimo  =-=-')

emprestimo=float(input('\nQual é o valor da casa que você deseja comprar:\nR$ '))
salario=float(input('Qual é seu salário:\nR$ '))
anos=int(input('Em quantos anos você deseja pagar esse empréstimo:\n'))

nparcelas=float((anos*12))
vparcela=float(emprestimo/nparcelas)
porcSal=float(salario*(30/100))

if(porcSal>vparcela):
    print('\nSeu empréstimo foi aprovado!')
    print('{:.0f} parcelas de R$ {:.2f}'.format(nparcelas,vparcela))
else:
    print('\nSeu empréstimo foi negado')