#Pergunte a velocidade de um carro, se ele ultrapassar 80km/h ele leva uma mula
#Multa de de R$ 7 por km ecedido

print('-=-=-=-=-=-=-=-')
print('Radar (80Km/h)')
print('-=-=-=-=-=-=-=-')

velocidade=float(input('\nQual a velocidade que vc está trafegando (Km/h): '))

if(velocidade>80):
    multa=float((velocidade-80)*7)
    print('\nVocê foi multado em R${:.2f} por estar a {}Km/h acima da velocidade permitida'.format(multa, (velocidade-80)))
else:
    print('\nContinue assim, boa viagem!')