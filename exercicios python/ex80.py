valores = []
for c in range(0,5):
    valor = int(input('Digite um valor : '))
    if not valores:
        valores.append(valor)
    else:
        pos = 0
        while pos < len(valores):
            if valor <= valores[pos]:
                break
            pos += 1
        valores.insert(pos, valor)

print(valores)