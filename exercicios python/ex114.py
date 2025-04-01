import requests

try:
    reposta = requests.get('https://www.youtube.com.br/')

except:
    print('\033[31mSite Pudim não está acessivel.\033[m')

else:
    print('\033[32mConsegui acessar o site Pudim com sucesso.\033[m')