ano = int(input('Digite um ano: '))
if ano % 4 == 0:
    if ano % 100 == 0 and ano % 400 == 0:
        print('ano bissexto')
    if ano % 100 != 0:
        print('ano bissexto')
    else:
        print('ano não bissexto')
else:
    print('ano não bissexto')