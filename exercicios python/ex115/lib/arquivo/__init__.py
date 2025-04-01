from ..interface import *

def ArquivoExiste(nome):
    try:
        a = open(nome, 'rt') # A função open tenta abrir um arquivo/ 'rt' significa que você vai abrir pra leitura do arquivo texto
        a.close() #close pra fechar o arquivo
    except FileNotFoundError:
        return False
    else:
        return True

def CriarArquivo(nome):
    try:
        a = open(nome, 'wt+') #'wt+' serve para criar arquivo
        a.close()
    except:
        print('Ouve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def LerArquivo(nome):
    try:
        a = open(nome, 'rt') # 'rt' serve para ler o arquivo
    except:
        print('Erro ao ler o arquivo')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<10}       {dado[1]:>10} anos')
                                                                #print(a.read())   #.read pra ler, com o print pra mostrar na tela/ #readlines cria uma lista pra mostrar no print
    finally:
        a.close()


def Cadastrar(arq,nome='desconhecido',idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro na hora de escrever os dados!')
        else:
            print(f'Cadastro de {nome} adicionado!')
        finally:
            a.close()