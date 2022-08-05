s = float(input('Digite o valor de seu salario:'))
if s > 1250.00:
    a = s * (10/100)
    ns = s + a
    print('Você recebeu um aumento de R$ {:.2f} \nSeu salario atual é R$ {:.2f}'.format(a, ns))
else:
    a = s * (15/100)
    ns = s + a
    print('Você recebeu um aumento de R$ {:.2f} \nSeu salario atual é R$ {:.2f}'.format(a, ns))
