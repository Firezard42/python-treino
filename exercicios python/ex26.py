f = str(input('Digite uma frase : ')).upper().strip()
print(f'A Letra \'A\' aparece : {f.count('A')} vezes')
print(f'A Letra \'A\' aparece pela primeira vez na posição {f.find('A')}')
print(f'A Letra \'A\' aparece pela última vez na posição {f.rfind('A')}')