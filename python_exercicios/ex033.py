n1 = int(input('digite um numero inteiro: '))
n2 = int(input('digite outro numero inteiro: '))
n3 = int(input('digite outro numero inteiro: '))

if n1 > n2 and n1 > n3:
    if n2 > n3:
        print('Os valores em ordem decrescente são: ',n1,n2,n3)
    else:
        print('Os valores em ordem decrescente são: ',n1,n3,n2)
elif n2 > n1 and n2 > n3:
    if n3 > n1:
        print('Os valores em ordem decrescente são: ',n2,n3,n1)
    else:
        print('Os valores em ordem decrescente são: ',n2,n1,n3)
else:
    if n1 > n2:
        print('Os valores em ordem decrescente são: ',n3,n1,n2)
    else:
        print('Os valores em ordem decrescente são: ',n3,n2,n1)