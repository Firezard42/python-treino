#OBS: ESSE CODIGO DESSE JEITO PODE MUDAR TODA SUA PASTA DE DOWNLOADS

import os #conversa com o sistema do seu computador (pastas, arquivos, etc).
import shutil #move arquivos de um lugar para outro.

pasta_downloads = os.path.join(os.path.expanduser("~"), "Downloads") # ~ é um atalho para a pasta do seu usuário no computador.
#.path.expanduser("~") = pega a pasta do usuário, tipo C:\Users\Neto no Windows.
#os.path.join(...) = junta isso com o nome "Downloads", de forma correta pro sistema.

tipos_arquivos = {
    "Imagens": [".png", ".jpg", ".jpeg", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Vídeos": [".mp4", ".avi", ".mov"],
    "Músicas": [".mp3", ".wav"],
    "Compactados": [".zip", ".rar"]
}

for pasta in tipos_arquivos:
    caminho = os.path.join(pasta_downloads,pasta)
    #"Junta o caminho da pasta Downloads com o nome da pasta que queremos criar."
    #exemplo : caminho = "C:/Users/Neto/Downloads/Imagens",o pasta vai significar qual parte do dicionario ele vai estar
    if not os.path.exists(caminho):
            #“Essa pasta já existe no computador?”
        os.mkdir(caminho)
            #Se a pasta não existir, então o Python cria ela usando mkdir

for arquivo in os.listdir(pasta_downloads): #os.listdir(...) = lista tudo que tem dentro de uma pasta./ os.listdir(pasta_downloads) vai devolver: ["foto.png", "musica.mp3", "trabalho.docx", "Vídeos"]
    caminho_arquivo = os.path.join(pasta_downloads,arquivo) #ele descobre onde está exatamente cada objeto na mochila.
    if os.path.isfile(caminho_arquivo): #“Esse item é mesmo um arquivo ou é uma pasta?” A gente só quer organizar arquivos, não pastas.
        nome, extensao = os.path.splitext(arquivo) #Aqui o Python separa o nome e a extensão do arquivo.

        for pasta, extensoes in tipos_arquivos.items(): #pasta e extensoes sao equivalentes a keys e values, lembre do comando .items
            if extensao.lower() in extensoes:
                novo_caminho = os.path.join(pasta_downloads, pasta, arquivo)
                shutil.move(caminho_arquivo,novo_caminho)
                print(f'Movendo {arquivo} para a pasta {pasta}')
                break