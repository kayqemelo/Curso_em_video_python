#Peça um frase ao usuario e mostre:
#quantas vezes aparece o 'a'
#em que posição aparece pela primeira e ultima vez

frase=str(input('Digite uma frase:\n')).strip().lower()

print('\nO caracter "a" aparece {} vezes'.format(frase.count('a')))
print('O caracter "a" apareceu pela primeira vez na posição {}'.format(frase.find('a')+1))
print('O caracter "a" apareceu pela ultima vez na posição {}'.format(frase.rfind('a')+1))