import math

a = float(input('Digite um ângulo: '))
a = (a*math.pi)/180
s = math.sin(a)
c = math.cos(a)
t = math.tan(a)
print(f'{s:.2f} {c:.2f} {t:.2f}')

#formula para mostrar na tela o valor do seno, cosseno e tangente do ângulo é :  angulo x pi / 180 para transformar primeiramente angulo em radiano para depois você conseguir usar a biblioteca math.
