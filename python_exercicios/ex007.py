n = str(input('Digite o nome do aluno: '))
print('Digite as notas de', n)
n1 = float(input('Nota de matemática:'))
n2 = float(input('Nota de Português:'))
m = (n1+n2)/2
print('O aluno {} recebeu a média de {:.1f}'.format(n,m))