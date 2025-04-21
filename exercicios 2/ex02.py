def palindromo(n):
    n2 = n.replace(' ','').lower()
    n2 = n2.split(',')
    n = n.split(',')
    print('Palíndromos \033[31mencontrados:\033[m ',end=' ')
    for e,c in enumerate(n2):
        c2 = c[::-1]
        if c2 == c:
            print(f'\033[32m{n[e]}\033[m',end=' -> ')
    print('\033[31mFIM\033[m')







palindromo(str(input('Digite quantas palavras ou frases quiser separadas por vírgula : ')).strip())