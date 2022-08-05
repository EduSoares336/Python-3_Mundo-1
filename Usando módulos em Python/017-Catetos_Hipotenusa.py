import math
ca = int(input('digite o valor do cateto adjacente:'))
co = int(input('Digite o valor do cateto oposto:'))
hip = math.hypot(ca,co)
print('Analisando os valores dos catetos {} e {}, o valor da hipotenusa é {:.2f}'.format(ca,co,hip))
