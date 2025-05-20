import pandas as pd
import openpyxl

df = pd.read_excel('vendas.xlsx') #lê o arquivo em excel

df['Total'] = df['Quantidade']*df['Preço Unitário'] #multiplica quantidade vs unitário e cria uma nova coluna chamada total

df.to_excel('vendas_atualizadas.xlsx', index=False) #cria um novo arquivo com a atualização que criamos do ['Total']