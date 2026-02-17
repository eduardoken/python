velocidade = float(input('Informe a velocidade em km do carro: '))
if velocidade > 80:
    print('Você foi multado, sua multa vai custar R${:.2f}'.format((velocidade - 80) * 7))
else:
    print('Está dentro do limite de velocidade')