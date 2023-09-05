#Faça um codigo que leia a largura e a altura de uma parede em metros. calcula a sua área a quantidade de tinta a
#necessÁria para pintá-la. sabando que cada litro de tinta. pinta uma área da 2m2.

n1=float(input('Altura da parede: '))
n2=float(input('Largura da parede: '))

x=float(n1*n2)
print('area da parede: {:.2f} m2'.format(x))
print('\nVamos utilizar {:.1f} litros de tinta para pintar essa parede' .format(x/2))