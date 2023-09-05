#Crie um programa que leia duas notas de um aluno e calcule sua média, 
#mostrando uma mensagem no final, de acordo com a média atingida:

print('-=-= Média Final =-=-')

n1=float(input('\nDigite a 1° nota: '))
n2=float(input('Digite a 2° nota: '))
n3=float(input('Digite a 3° nota: '))

media=float((n1+n2+n3)/3)

if(media>10 or media<0):
    print('\nNota inválida :|')
if(media>=8 and media<=10):
    print('\nAprovado, você foi muito bem!!!')
    print('Média: {:.1f}'.format(media))
elif(media>=6 and media<8):
    print('\nAprovado')
    print('Média: {:.1f}'.format(media))
elif(media>5 and media<6):
    print('\nRecuperação')
    print('Média: {:.1f}'.format(media))
elif(media>0 and media<5):
    print('\nReprovado :(')
    print('Média: {:.1f}'.format(media))



