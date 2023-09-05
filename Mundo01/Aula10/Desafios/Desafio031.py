#Pergunte a distancia de uma viagem em Km, calcule o preço da passagem, cobrando R$0,50 por Km para
#viagens até 200 Km e R$0,45 para viagens longas 

print('-=-=-= VIAGENS =-=-=-')

distancia=float(input('Sua vaigem é de quantos Km? '))

if(distancia<200):
    valor=float(distancia*0.50)
    print('\nO valor da sua viagem será R${:.2f}'.format(valor))
else:
    valor2=float(distancia*0.45)
    print('\nO valor da sua viagem será R${:.2f}'.format(valor2))