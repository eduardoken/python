"""nome = str(input('Informe o seu nome: '))
if nome == 'Eduardo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}'.format(nome))"""

n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
media = (n1 + n2) / 2
print('A sua média é {:.1f}'.format(media))
if media >= 6:
    print('Sua média é alta')
else:
    print('Sua média é baixa')