n = str(input('Digite seu nome completo : ')).strip().title()
n = n.split()
print(f'First Name: {n[0]}')
n2 = len(n) - 1
print(f'Last name : {n[n2]}')
