'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do 
Campeonato Brasileiro de Futebol,na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.'''

print('-=-= Tabela Brasileirão =-=-')

tabela = ('Botafogo', 'Grêmio', 'Flamengo', 'Palmeiras', 'Athletico-PR', 'São Paulo (maior do Brasil)',
          'Fluminense', 'RB-Bragantino', 'Fortaleza', 'Internacional', 'Cruzeiro', 'Cuiabá', 'Atlético-MG',
          'Santos', 'Gambá', 'Goias', 'Bahia', 'Coritiba', 'América-MG', 'Vasco')

print('\nO que você deseja ver:')

while (True):
    print('\n[1] Os 5 primeiros times\n[2] Os últimos 4 colocados\n[3] Times em ordem alfabética')
    print('[4] Posição São Paulo\n[5] Sair')

    escolha = int(input(': '))
    if (escolha == 1):
        print('\n5 primeiros colocados:\n')
        print(tabela[0:5])
    elif (escolha == 2):
        print('\n4 ultimos colocados:\n')
        print(tabela[-4:])
    elif (escolha == 3):
        print('\nTimes em ordem alfabética:\n')
        print(sorted(tabela))
    elif (escolha == 4):
        print('\nPosição São Paulo:\n')
        posicaoSaoPaulo = tabela.index('São Paulo (maior do Brasil)')
        print(f'O São Paulo está na {posicaoSaoPaulo}° posição')
    elif (escolha == 5):
        break
    else:
        print(f'\Opção {escolha} inválida :(')


print('\nFim!!!')
