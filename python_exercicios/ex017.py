print('Informe as medidas dos catetos do triângulo: ')
ca = float(input('Qual a medida do cateto adjacente: '))
co = float(input('Qual a medida do cateto oposto: '))

h = (ca ** 2 + co ** 2) ** (1/2)
print('A hipotenusa de {} e {} é {}'.format(ca, co, h))