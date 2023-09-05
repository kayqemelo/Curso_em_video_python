'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma 
lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos
os valores únicos digitados, em ordem crescente.'''

print('-=-= Lista de valores =-=-\n')
lista = []
cont = 1

while (True):

    x = int(input(f'Digite o {cont}° valor: '))

    if (x not in lista):
        lista.append(x)
    else:
        print(f'\nO valor {x} é repetido, não será adicionado')
        r = str(input('Deseja continuar[S/N]: ')).strip().upper()[0]
        if (r == 'N'):
            break
        else:
            cont = cont-1

    cont = cont+1

lista.sort()
print(f'\nLista final:\n{lista}')
