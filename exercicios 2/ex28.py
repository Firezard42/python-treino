#Q5. Calcular valores de Q a partir de D
#Crie uma função Python que calcule o valor de ( Q ) usando a fórmula:
#q = √(2 * C * D) / H
#onde ( C ) é 50 e ( H ) é 30. A função deve receber apenas ( D ) como entrada, que consiste em uma sequência de valores separados por vírgulas. A saída deve ser arredondada para o inteiro mais próximo e impressa em uma única linha, separada por vírgulas.

import math

def valor_q(lista):
    lista2 = list()
    c = 50
    h = 30
    for i in lista:
        q = round(math.sqrt((2*c*i)/h))
        lista2.append(q)
    return lista2


lista = list()
for i in range(1,4):
    d = float(input(f'Digite o {i}º valor de D:'))
    lista.append(d)

print(valor_q(lista))