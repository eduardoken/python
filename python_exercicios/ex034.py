s = float(input('Informe o seu salario: '))

if s <= 1250:
    a = s + s * 15 / 100
    print("O seu salario com o aumento será de: {}".format(a))
else:
    a = s + s * 10 / 100
    print("O seu salario com o aumento será de: {}".format(a))