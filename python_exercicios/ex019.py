from random import choice
p1 = input('Primeiro nome: ')
p2 = input('Segundo nome: ')
p3 = input('Terceiro nome: ')

e = choice([p1, p2, p3])

print ('O escolhido foi {}'.format(e))
