d = float(input('Informe a distância a percorrer em km: '))
if d > 200:
    d = d * 0.45
    print('O preço da passagem será de R${:.2f}'.format(d))
else:
    d = d * 0.5
    print('O preço da passagem será de R${:.2f}'.format(d))