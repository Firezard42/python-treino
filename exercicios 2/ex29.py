#Crie um programa em Python que receba dois dígitos, Me N, como entradas e gere um array bidimensional.
# O valor na i-ésima linha e na j-ésima coluna do array deve ser .i*j

def matriz_tabela(linha,coluna):
    matriz = []
    for c in range(linha):
        linha = []
        for c2 in range(coluna):
            linha.append(c*c2)
        matriz.append(linha)
    return matriz


l = int(input('Quantas linhas você quer na matriz  ? '))
c = int(input('Quantas colunas você quer na matriz ?'))

matriz = matriz_tabela(l,c)

for c in (matriz):
    print(c)