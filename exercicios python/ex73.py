tabela = ('Botafogo','Palmeiras','Flamengo','Fortaleza','Internacional','São Paulo','Corinthians','Bahia','Cruzeiro','Vasco',
          'Vitória','Atlético-MG','Fluminense','Grêmio','Juventude','Red Bull Bragantino','Athletico-PR','Criciúma','Atlético-GO','Cuiabá')

print('Os 5 primeiros colocados:')
for c in range(0,len(tabela)):
    if c <= 4:
        print(f'\033[32m{c+1}º{tabela[c]}\033[m')

print('='*50)
print('Os 4 últimos colocados:')
for c in range(0, len(tabela)):
    if c >= 16:
        print(f'\033[31m{c+1}º{tabela[c]}\033[m')


print('='*50)
print('Tabela em ordem alfabética')
print(sorted(tabela))

print('='*50)
print(f'Posição do Time Flamengo : {tabela.index('Flamengo')+1}º posição.')