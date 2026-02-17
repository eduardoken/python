from random import randint

r = randint(0, 5)

n = int(input('Informe um número de 0 a 5 e tente acertar o numero aleatório gerado: '))

if n == r:
    print('Acertou parabéns')
else:
    print('Errou o numero certo era {}'.format(r))