import random
print('Vou pensar em um número de 0 a 5. \nTente advinhar!')
ln = ['0','1','2','3','4','5']
n = input('Em que número pensei?')
if random.choice(ln) == n:
    print('Você venceu!')
else:
    print('Você perdeu!')
