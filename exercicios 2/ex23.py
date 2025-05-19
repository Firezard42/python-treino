lista = [1,3,5]
lista2 = list()

for c in lista:
    n = c
    for c2 in range(1,3):
        n = n * c
    lista2.append(n)

print(lista2)

