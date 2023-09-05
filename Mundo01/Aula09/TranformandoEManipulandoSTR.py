#Transformando str

frase = 'Curso em Video Python'
#       "0123456789...       "

#Metodo "replace" (faz a troca de palavras)
print(frase.replace('Python', 'Android'),'\n')

#Metodo "upper" (Deixa tudo maiusculo)
print(frase.upper(),"\n")

#Metodo "lower" (Deixa tudo minusculo)
print(frase.lower(),'\n')

#Metodo "capitalize" (Deixa tudo minusculo, menos o primeiro caracter da str)
print(frase.capitalize(),'\n')

#Metodo "title" (deixa todas as primeiras letras das palavras maiusculas)
print(frase.title(),'\n')

#Metodo "strip" (retira os espaços inuteis no inicio e fim da str)
frase2 = '   Kayque Melo   '
print(frase2.strip(),'\n')

#Metodo "rstrip" (retira os espaços inuteis da direita "r" da str)
print(frase2.rstrip(),'\n')

#Metodo "lstrip" (retira os espaços inuteis da esquerda "l" da str)
print(frase2.lstrip(),'\n')

#Metodo "split" (divide a str em str menores, dividindo-as pelos espaços e enumera essas novas str)
print(frase.split(),'\n')

#Metodo "join" (Junta diferentes strings de uma lista em apenas uma)
print(''.join(frase))


