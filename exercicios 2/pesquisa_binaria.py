def pesquisa_binaria(lista,item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo+alto) // 2 # a divisão com // evitar que o numero meio seja um numero float
        chute = lista[meio]
        #print(alto)
        #print(meio)
        #print(chute)
        #print('=='*10)

        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        if chute < item:
            baixo = meio + 1
    return None

minha_lista = [1,3,5,7,9]


print(f'A posição do seu item é : {pesquisa_binaria(minha_lista,-1)}')
print(f'A posição do seu item é : {pesquisa_binaria(minha_lista,3)}')