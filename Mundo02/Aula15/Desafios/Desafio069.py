'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa 
deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''

print('-=-= Análise de dados do grupo =-=-')
contidade=conth=contm=0

while(True):

    nome=str(input('\nDigite seu nome: ')).strip()
    idade=int(input('Digite sua idade: '))

    if(idade>=18):
        contidade+=1

    sexo=str(input('Digite seu sexo[M/F]: ')).strip().upper()[0]

    if(sexo=='M'):
        conth+=1

    elif(sexo=='F' and idade>=20):
        contm+=1

    continuar=str(input('\nDeseja continuar[S/N]: ')).strip().upper()[0]

    if(continuar=='N'):
        break

print('\nFim...')
print(f'{contidade} pessoa(s) tem mais ou 18 anos')
print(f'Foram cadastrado(s) {conth} homens')
print(f'Foram cadastrado(s) {contm} mulheres com 20 anos ou mais')