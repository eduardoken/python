frase = input('Digite uma frase: ')
l = 1 + frase.find('A')
r = 1 + frase.rfind('A')
print('A frasse possui {} letras A'.format(frase.count('A')))
print('A letra A se inicia na {}° posição'.format(l))
print('A letra A se termina na {}° posição'.format(r))
#a maiuscula
