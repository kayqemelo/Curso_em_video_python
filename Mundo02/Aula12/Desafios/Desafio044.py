#Elabore um programa que calcule o valor a ser pago por um produto, 
#considerando o seu preço normal e condição de pagamento:
#-à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros

print('-=-= CAIXA =-=-')

valor=float(input('\nQual é o valor total das suas compras:\nR$'))

print('\n-=-= Opções de pagamento =-=-')
print('[1] à vista dinheiro/cheque')
print('[2] à vista no cartão')
print('[3] em até 2x no cartão')
print('[4] 3x ou mais no cartão')
op=int(input('Opção: '))

if(valor<=0):
    print('\nValor inválida')
elif(op==1):
    print('\nValor a pagar R${}'.format(valor-(valor*0.10)))
elif(op==2):
    print('\nValor a pagar R${}'.format(valor-(valor*0.05)))
elif(op==3):
    print('\nValor a pagar R${}'.format(valor))
elif(op==4):
    print('\nValor a pagar R${}'.format(valor+(valor*0.20)))
else:
    print('\nOpção inválida')