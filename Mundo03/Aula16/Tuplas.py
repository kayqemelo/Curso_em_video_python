'''Tuplas são imútaveis (não pode mudar os valores dentro dela)'''

lanche = ('Hamburgue', 'Suco', 'Pizza', 'Pudim')

print(lanche[0]+'\n')


for comida in lanche:
    print(f'Gosto muito de {comida}')


print('///////////////////////')


for cont in range(0, len(lanche)):
    print(f'Vou comer {lanche[cont]}') 
