#Faça um algoritmo que leia o preço de um produto e mostre seu novo preco. com 5% de desconto.

print('--- Desconto 5% ---')
n1=float(input('\nDigite o preço do produto: '))

desconto=float((n1*5)/100)

print('Preço com desconto: {}'.format(n1-desconto))
