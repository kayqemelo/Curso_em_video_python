#Crie um programa que diga se o seu nome tem silva

nome=str(input('Digite seu nome completo:\n')).strip()

print('\nO seu nome tem Silva?')
print('silva' in nome.lower())