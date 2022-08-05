a, b, c = input('Digite três valores diferentes:').split()
a = int(a)
b = int(b)
c = int(c)
if a > b and a > c:
    print('O valor {} é o maior'.format(a))
else:
    if b > a and b > c:
        print('O valor {} é o maior'.format(b))
    else:
        print('O valor {} é o maior'.format(c))
if a < b and a < c:
    print('E o valor {} é o menor'.format(a))
else:
    if b < a and b < c:
        print('E o valor {} é o menor'.format(b))
    else:
        print('E o valor {} é o menor'.format(c))
