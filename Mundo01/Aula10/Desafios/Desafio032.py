#peça um ano e determine se ele é bisexto ou não

print('-=-= O ano é bisexto? =-=-\n')
ano=int(input('Digite algum ano: '))

if(ano%4==0 and ano%100!=0 or ano%400==0):
    print('\nO ano de {} é bisexto'.format(ano))
else:
    print('\nO ano de {} não é bisexto'.format(ano))