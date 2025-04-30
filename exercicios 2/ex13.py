import unidecode

semana = ['segunda','terça','quarta','quinta','sexta','sabado','domingo']

dia = str(input('Qual é o dia da semana ? ')).strip().lower()
dia2 = unidecode.unidecode(dia) #para remover acento das palavras.

if dia2 == semana[5] or dia == semana[6]:
    print(f'{dia} é dia do descanso')

elif dia in semana:
    print(f'{dia} é dia de trabaia')

else:
    print('opção inválida')