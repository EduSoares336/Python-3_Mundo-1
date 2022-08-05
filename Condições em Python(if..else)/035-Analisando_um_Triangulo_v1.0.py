r1, r2, r3 = input('Digite valores de três retas:').split()
r1 = int(r1)
r2 = int(r2)
r3 = int(r3)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Com esses valores é possivel formar um triângulo!')
else:
    print('Não é possivel formar um triângilo com esses valores!')
