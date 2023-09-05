#Crie um programa que diga se a cidade que vc nasceu se inicia com santo ou não

cidade = str(input('Digite a cidade em que você nasceu:\n')).strip()

print('')
print(cidade[:5].lower() == 'santo')