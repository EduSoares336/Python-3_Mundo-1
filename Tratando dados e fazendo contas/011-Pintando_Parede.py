largura = float(input('Largura da parede:'))
altura = float(input('Altura da parede:'))
area = largura * altura 
tinta = area / 2
print('A área dessa parede mede {:.2f}m².'.format(area))
print('Para pintar essa parede, é necessario {:.2f}l de tinta.'.format(tinta))
