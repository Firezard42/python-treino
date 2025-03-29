def moeda(n):
    n = f'{n:.2f}'
    n2 = str(n)
    n2 = n2.replace('.',',')
    return f'R${n2}'

def metade(n,f = False):
    n = n/2
    if f: #if f significa se for True
        n = moeda(n)
        return n
    else:
        return n

def dobro(n,f = False):
    n = n*2
    if f:
        n = moeda(n)
        return n
    else:
        return n

def aumentar(n,p = 0,f = False):
    p2 = (n*p) / 100
    n = n+p2
    if f:
        n = moeda(n)
        return n
    else:
        return n

def diminuir(n,p = 0,f = False):
    p2 = (n*p) / 100
    n = n - p2
    if f:
        n = moeda(n)
        return n
    else:
        return n

def resumo(n,p1 = 0,p2 = 0):
    d = dobro(n,True)
    m = metade(n,True)
    aumentar1 = aumentar(n,p1,True)
    diminuir2 = diminuir(n,p2,True)
    print('-'*45)
    print('RESUMO DO VALOR'.center(40))
    print('-'*45)
    print(f'{'Preço analisado:':<20} {moeda(n):>20}')
    print(f'{'Dobro do preço:':<20} {d:>20}')
    print(f'{'Metade do preço:':<20} {m:>20}')
    print(f'{f'{p1}% de aumento:':<20} {aumentar1:>20}')
    print(f'{f'{p2}% de redução:':<20} {diminuir2:>20}')
    print('-'*45)