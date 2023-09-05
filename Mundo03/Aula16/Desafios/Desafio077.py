'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, 
você deve mostrar, para cada palavra, quais são as suas vogais.'''
print('-=-= Vogais =-=-\n')
tupla = ('carro', 'cerveja', 'ovo', 'cinuca', 'uva', 'brinco')

for cont in tupla:
    print(f'\nNa palavra {cont} temos:', end=' ')

    for letra in cont:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
