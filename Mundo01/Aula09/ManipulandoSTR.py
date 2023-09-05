#Manipulando textos

frase =  'Curso em Video Python'
#        "0123456789...       "

#Fatiamento pegando um indice (letra "V" nesse caso)
print(frase[9])

#Fatiamento para pegar uma cadeia de caracteres, sempre um a menos (cadeia "Video")
print('\n'+frase[9:14])

#Fatiando a frase pegando des do inicio (cadeia "Curso")
print('\n'+frase[:6])

#Fatiando a frase pegando até o fim (cadeia "Python")
print('\n'+frase[15:])

#Fatiando pilandp caracteres (utlizamos o x:x:Y)
print('\n'+frase[::2])