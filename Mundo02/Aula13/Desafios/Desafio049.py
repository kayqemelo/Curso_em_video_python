#Faça uma tabuada utilizando FOR
print('-=-= Tabuada =-=-')
x=int(input('Descubra a tabuada do: '))
print('')
for cont in range(0,11):
    print('{} x {} = {}'.format(x,cont,(cont*x)))