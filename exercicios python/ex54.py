import datetime

maior = 0
menor = 0

for c in range(1,8):
    nasc = int(input('Digite o ano que você nasceu : '))
    idade = datetime.datetime.now().year - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1

print(f'{menor} Pessoas não atingiram a maior idade')
print(f'{maior} já são de maior')