ano = int(input('Digite um ano qualquer : '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 100 == 0 and ano % 400 == 0:
    print('esse ano é bissexto')
else:
    print('não bissexto')