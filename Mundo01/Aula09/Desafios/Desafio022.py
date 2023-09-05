#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com letras maiusculas e minusculas
#Quantidade de letras em contar espaços
#Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome:\n')).strip()

print('\nSeu nome com letras maiusculas:\n{}'.format(nome.upper()))

print('\nSeu nome com letras minusculas:\n{}' .format(nome.lower()))

print('\nSeu nome tem {} letras' .format(len(nome)-nome.count(' ')))

print('\nSeu 1° nome tem {} letras' .format(nome.find(' ')))

separa=nome.split()
print('\nSeu primeiro nome é {} e ele tem {} letras' .format(separa[0], len(separa[0])))