print('-=-= Lista =-=-')

comidas = ['bolo', 'sorvete', 'pão', 'pudim']

print(f'\n{comidas}')
print(comidas[1])

'como adicionar mais um elemento a lista'
print('\nAdicionando mais um item no final da lista')
comidas.append('cokkie')
print(comidas)

'Como inserir mais um item em qualquer posição da lista'
print('\nAdicionando mais um item em qualquer posição da lista')
comidas.insert(0, 'uva')
print(comidas)

'Como remover algum item da lista'
print('\nRemovendo item da lista por posição')
'Função pop sem especificar elimina o ultimo item'
comidas.pop(3)
print(comidas)

print('\nRemovendo item da lista por nome')
comidas.remove('pudim')
print(comidas)
