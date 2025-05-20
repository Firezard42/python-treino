import asyncio
from googletrans import Translator

async def traduzir_texto():
    tradutor = Translator()
    texto = input("Digite um texto para traduzir: ")
    traducao = await tradutor.translate(texto, src='pt', dest='en')
    print("Tradução:", traducao.text)

asyncio.run(traduzir_texto())