#Pergunte ao usuario seu nome e retonr o ptimeiro e ultimo

nome=str(input('Digite seu nome:\n')).strip()

lista=nome.capitalize().split()
print('\n',lista)
print('\nSeu primeiro nome é {}'.format(lista[0]))
print('Seu ultimo nome é {}'.format(lista[len(lista)-1]))

