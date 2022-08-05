import math
n = int(input('Digite um número: '))
rad = math.radians(n)
print('Analisando o número {}, \nseu seno é {:.2f}, \nseu cosseno é {:.2f} e \nsua tangente é {:.2f}'.format(n,math.sin(rad),math.cos(rad),math.tan(rad)))
