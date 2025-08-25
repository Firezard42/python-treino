#Crie um programa em Python que identifique todos os números entre 100 e 300 (inclusive) que são divisíveis por 7,
# mas não múltiplos de 5. Os números identificados devem ser exibidos em uma única linha, separados por vírgulas.

num = []

for c in range(100,201):
    if c % 7 == 0 and c % 5 != 0:
        num.append(c)

print(num)