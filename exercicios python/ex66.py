cont = 0
soma = 0

while True:
    n1 = float(input('Digite um valor (\033[31mdigite 999 pra parar\033[m): '))
    if n1 == 999:
        break
    else:
        cont += 1
        soma = soma+n1

print(f'Foram digitados {cont} números e a soma deles é {soma}!')