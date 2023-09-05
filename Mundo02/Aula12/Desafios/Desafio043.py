#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal
#(IMC) e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida

print('-=-= IMC =-=-\n')

print('digite os seguintes valores:')
peso=float(input('Peso: '))
altura=float(input('Altura: '))
print()
imc=float(peso/(altura*altura))


if(imc<18.5 and imc>0):
       print('Abaixo do peso, IMC {:.1f}'.format(imc))
elif(imc>=18.5 and imc<25):
        print('Peso ideal, IMC {:.1f}'.format(imc))
elif(imc>=25 and imc<30):
        print('Sobre peso, IMC {:.1f}'.format(imc))
elif(imc>=30 and imc<40):
        print('Obesidade, IMC {:.1f}'.format(imc))
elif(imc>=40):
        print('Obesidade morbida, IMC {:.1f}'.format(imc))
else:
        print('Valores inválidos!!!')