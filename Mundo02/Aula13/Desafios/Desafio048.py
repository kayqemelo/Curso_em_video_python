#Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que 
#se encontram no intervalo de 1 até 500.


print('Soma entre todos os números impares que são múltiplos de três e que se encontram \nno intervalo de 1 até 500\n')
x=int(0)
for cont in range(1,501,2):
  if(cont%3==0):
    x = x+cont 
    
print('\nA soma de todos os valores solicitados é {}'.format(x))