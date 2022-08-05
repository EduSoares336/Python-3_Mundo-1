vm = int(input('Digite a velocidade do carro:'))
if vm > 80:
    print('Você ultrapassou a velocidade media.')
    print('Sua multa é de R${:.2f} .'.format((vm - 80)* 7))
else:
    print('Não ultrapassou o limite de velocidade, continue assim.')
