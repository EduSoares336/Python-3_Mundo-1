salario = float(input('Qual o salario do funcionário?'))
aumento = (salario * 15) / 100
salario2 = salario + aumento
print('O funcionário que tinha salario de R${:.2f}, com o aumento de 15%, irá receber agora R${:.2f}'.format(salario, salario2))
