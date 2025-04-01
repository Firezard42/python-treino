from time import sleep
from lib.interface import *
from lib.arquivo import *

arq = 'Cursoemvideo.txt'

if not ArquivoExiste(arq):
    CriarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas','Cadastrar nova Pessoa','Sair do Sistema'])
    if resposta == 1:
        LerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip()
        idade = LeiaInt('Idade: ')
        Cadastrar(arq,nome,idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema...Até logo!')
        break
    sleep(2)