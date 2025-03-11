pilha = []
n1 = str(input('digite a expressão : '))
for c in n1:
    if c == '(':
        pilha.append('(')
    if c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão está correta')
else:
    print('Sua expressão está incorreta')