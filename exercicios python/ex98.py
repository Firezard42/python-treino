from time import sleep
def contador(i,f,p):
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    if f < i:
        if p > 0:
            p = p * -1
        for c in range(i, f-1, p):
            print(c, end=' ')
            sleep(0.5)
    else:
        for c in range(i,f+1,p):
            print(c,end=' ')
            sleep(0.5)
    print('')

contador(1,10,1)
contador(10,0,2)
n1 = int(input('Início : '))
n2 = int(input('Fim : '))
p1 = int(input('Passo : '))
contador(n1,n2,p1)