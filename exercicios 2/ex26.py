#Crie uma função Python que receba uma sequência de números separados por vírgulas como entrada e gere uma lista e uma tupla contendo esses números.

n = str(input('Digite vários números separados por vírgula: '))

n2 = n.split(',')

print(n2)

n3 = tuple(n2)

print(n3)