preço = float(input('Qual é o preço do produto?'))
desconto = (preço * 5) / 100
preço2 = preço - desconto
print('O produto que custava R${:.2f}, com um desconto de 5%, irá custar agora R${:.2f}'.format(preço, preço2))
