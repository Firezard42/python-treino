#Crie uma função Python que receba um inteiro ( n ) como entrada e gere um dicionário contendo pares ( (i, i^2) )
# para todos os inteiros ( i ) de 1 a ( n ) (inclusive). A função deve então retornar este dicionário.

def generate_square_dict(n):
    dic = {}

    for c in range(1,n+1):
        dic[c] = c**2

    return dic


resp = generate_square_dict(n= int(input('Digite um número inteiro: ')))
print(resp)