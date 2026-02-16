from random import shuffle
p1 = input('Primeiro nome: ')
p2 = input('Segundo nome: ')
p3 = input('Terceiro nome: ')
p4 = input('Quarto nome: ')

e = [p1, p2, p3, p4]

shuffle(e)

print ('O escolhido foi {}'.format(e))
