from datetime import date
ano = int(input('Digite o ano que você quer analizar(caso digite o valor 0, o ano sera o atual):'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto!'.format(ano))
else:
    print('O ano {} não é Bissexto'.format(ano))
