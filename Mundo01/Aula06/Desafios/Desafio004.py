#Faça um programa que leia algo e nostre seu tipo primitivo e todas suas informações

n1=input('Digite alguma coisa: ')
print()
print(n1)
print('Tipo primitivo',type(n1))
print('É composto só por espaços:', n1.isspace())
print('É um número:', n1.isnumeric())
print('É alfabetico:', n1.isalpha())
print('É alfanumerico:', n1.isalnum())
print('Esta em maiusculo:', n1.isupper())
print('Esta em minusculo:', n1.islower())
print('Esta capitalizada (Tem letras maiusculas e min):',n1.istitle())