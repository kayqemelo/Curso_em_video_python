lista = []

for cont in range(0, 5):
    lista.append(int(input('Digite um valor: ')))

print('')
for c, v in enumerate(lista):
    print(f'Na posição {c} encontrei o valor {v}')

print('fim')
