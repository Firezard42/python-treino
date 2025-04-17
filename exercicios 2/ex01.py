from string import punctuation

frase2 = dict()
frase = str(input('Digite uma frase: ')).strip(punctuation).strip().lower().split()
for c in range(0,len(frase)):
    n = frase[c]
    if frase[c] not in frase2:
        frase2[frase[c]] = frase.count(n)
print(frase2)