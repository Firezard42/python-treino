from idlelib.replace import replace


def moeda(n):
    n = f'{n:.2f}'
    n2 = str(n)
    n2 = n2.replace('.',',')
    return f'R${n2}'

def metade(n):
    n = n/2
    n2 = moeda(n)
    return n2

def dobro(n):
    n = n*2
    n2 = moeda(n)
    return n2

def aumentar(n,p = 0):
    p2 = (n*p) / 100
    n = n+p2
    n2 = moeda(n)
    return n2

def diminuir(n,p = 0):
    p2 = (n*p) / 100
    n = n - p2
    n2 = moeda(n)
    return n2