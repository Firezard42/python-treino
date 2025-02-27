soma = 0
n1 = 0
for c in range(1,501):
    if c % 2 != 0:
        if c % 3 == 0:
            soma = c+soma
            n1 = n1+1

print(f'{n1} números localizados, a soma deles é {soma}')