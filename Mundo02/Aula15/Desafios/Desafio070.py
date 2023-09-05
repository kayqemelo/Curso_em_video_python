'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o 
usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''

print('-=-= Compras =-=-')
cont=1
maisBarato=total=caro=0

while(True):

    produto=str(input(f'\nDigite o nome do {cont}° produto: ')).split()

    preco=float(input('Preço R$ '))
    total+=preco
    if(preco>=1000):
        caro+=1

    sair=str(input('Deseja adicionar mais produtos[S/N]: ')).strip().upper()[0]

    maisBarato=preco
    nomebarato=produto

    if(preco<maisBarato):

        maisBarato=preco
        nomebarato=produto

    if(sair!='S'):
        break

    cont+=1

print(f'\nTotal da copra R$ {total:,.2f}')
print(f'Produto mais barato: {nomebarato} / Preço R$ {maisBarato:,.2f}')
print(f'{caro} produto(s) custam R$ 1000.00 ou mais')