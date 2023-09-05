#Vamos analisar e tirar informações da string

frase = 'Curso em Video Python'
#       "0123456789...       "

#Metodo "len" (conta o número de caracteres contando o 0)

print(len(frase),'\n')

#Função "count" (conta a quabtidade de caracteres sugeridos)

print(frase.count('o'),'\n')

#Função "count" com fatiamento (conta a quabtidade de caracteres sugeridos dentro de uma porção limitada)

print(frase.count('o',0,14),'\n')

#Função "find" (mostra quando começa qualquer conjunto de caracteres)

print(frase.find('Video'),'\n')

#Função "find" quanto nã encontra o conjunto retorna (-1)
print(frase.find('android',),'\n')

#Operador "in" (Retorna um booleano sobre a existencia do conjunto ou caracter)

print('Curso' in frase)