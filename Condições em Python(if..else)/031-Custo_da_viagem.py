km = float(input('Qual a distancia da viagem(em Km)?'))
if km > 200:
    p = km * 0.45
    print('A passagem custa R$ {:.2f}'.format(p))
else:
    p = km * 0.50
    print('A passagem custa R$ {:.2f}'.format(p))
