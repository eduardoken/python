r1 = int(input('Digite o valor do primeira reta: '))
r2 = int(input('Digite o valor do segunda reta: '))
r3 = int(input('Digite o valor do terceira reta: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('As retas podem formar um triângulo!')
else:
    print('As retas não podem formar um triângulo!')