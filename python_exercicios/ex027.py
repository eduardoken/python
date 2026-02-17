nome = str(input('Digite seu nome completo: '))
print('Seu nome é {}'.format(nome))
nome = nome.split()
print('Logo seu primeiro nome é {} e o útilmo é {}'.format(nome[0],nome[-1]))