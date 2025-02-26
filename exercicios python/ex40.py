n1 = float(input('Digite a primeira nota do aluno : '))
n2 = float(input('Digite a segunda nota do aluno : '))
media = (n1+n2)/2

if media < 5:
    print(f'Sua média foi {media} e você foi \033[0;31mREPROVADO\033[m!!!')

elif media >= 5 and media <= 6.9:
    print(f'Sua média foi {media} e você está em \033[0;33mRECUPERAÇÃO\033[m')

else:
    print(f'Sua média foi {media} e você foi \033[0;32mAPROVADO\033[m!!!')