'''Criando lita com a função list'''
print('Criando lita com a função list')
valores = list(range(4, 11))
print(valores)

'''Organizando valores em uma lista (Crescente)'''
print('\nOrganizando valores em uma lista')
valores = [2, 5, 8, 9, 10, 2, 1]
valores.sort()
print(valores)

'''Organizando valores em uma lista (Decresente)'''
print('\nOrganizando valores em uma lista (Decresente)')
valores = [2, 5, 8, 9, 10, 2, 1]
valores.sort(reverse=True)
print(valores)

'''Descobrindo tamanho das listas'''
print('\nDescobrindo tamanho das listas')
valores = [2, 5, 8, 9, 10, 2, 1]
print(f'Essa lista tem {len(valores)} valores')
