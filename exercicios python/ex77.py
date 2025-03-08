palavras  = ('aprender','programar','linguagem','python','curso','gratis','estudar','praticar','trabalhar','mercado','programador','futuro')

for c in palavras:
    print(f'Na Palavra {c.upper()} temos ás vogais : ',end=' ')
    for c2 in c:
        if c2 in 'aeiou':
            print(f'{c2}',end=' ')
    print('')