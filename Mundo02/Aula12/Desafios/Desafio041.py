#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa 
#que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade
#Até 9 anos: MIRIM– Até 14 anos: INFANTIL– Até 19 anos: JÚNIOR– Até 25 anos: SÊNIOR 
#– Acima de 25 anos: MASTER
from datetime import date
print('-=-= Classificação dos atletas =-=-')

nascimento=int(input('Idade de nascimento: '))
ano = date.today().year

idade=int(ano-nascimento)

print('')
if(idade>=0 and idade <=4):
    print('Idade não permitida para partcipar')
elif(idade<=9 and idade>=5):
    print('Categotia Mirin, idade {:.1f} anos'.format(idade))
elif(idade<=14 and idade>9):
    print('Categotia Infantil, idade {} anos'.format(idade))
elif(idade<=19 and idade>14):
    print('Categotia Junior, idade {} anos'.format(idade))
elif(idade<=25 and idade>19):
    print('Categotia Senior, idade {} anos'.format(idade))
elif(idade>25 and idade<=130):
    print('Categotia Master, idade {} anos'.format(idade))
elif(idade>130 or idade<0):
    print('Idade inválida!!!')