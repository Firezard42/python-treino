import time
n = int(input('Digite um número do 0 ao 9999 : '))
u = n // 1 % 10  # // <- simbolo de divisão, já o % é pra dar o resto da divisão
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Analisando o número enviado',end='')
time.sleep(0.3)
print('.',end='')
time.sleep(0.3)
print('.',end='')
time.sleep(0.3)
print('.')
print(f'Unidade : {u}')
print(f'Dezena : {d}')
print(f'Centena : {c}')
print(f'Milhar : {m}')