#numero = input(str('Digite um número:'))
#print('unidade:{}'.format(numero[3]))
#print('dezena:{}'.format(numero[2]))
#print('centena:{}'.format(numero[1]))
#print('milhar:{}'.format(numero[0]))
num = int(input('Digite um número:'))
n = num // 1 % 10
u = num // 10 % 10
m = num // 100 % 10
e = num  // 1000 % 10
print('unidade: {}'.format(n))
print('dezena: {}'.format(u))
print('centena: {}'.format(m))
print('milhar: {}'.format(e))
