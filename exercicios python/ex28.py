import random
import time
from random import randint

print('SOU O COMPUTADOR E ESTOU PENSANDO EM UM NÚMERO',end='')
time.sleep(0.5)
print('.',end='')
time.sleep(0.5)
print('.',end='')
time.sleep(0.5)
print('.')
n1 = int(input('FALAAA COMIGOOO, QUE NÚMERO EU PENSEI ???  '))
n2 = randint(0,5)

if n1 == n2:
    print(f'ACERTOUUU MIZERAVIIIII !!!!, o número pensado foi o {n2}')
else:
    print(f'que burooo da 0 pra ele, eu pensei no número {n2}')