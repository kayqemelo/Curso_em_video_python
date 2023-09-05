#Escreva um programa sobre aluguel de carros, pergunte os km e dias rodadas
#Faça o calculo sabendo que sera cobrado R$60 por dia e R$0,15 por KM rodado

print('              --- AlugCar ---\n')
dias=int(input('Quantos dias o carro ficou sobre sua posse:\n'))
km=float(input('Quantos Km foram rodados:\n'))

print('Total a pagar: {:.2f}'.format((dias*60)+(km*0.15)))
