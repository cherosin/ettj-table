import requests
import json
from bs4 import BeautifulSoup

url = 'https://www.anbima.com.br/informacoes/est-termo/CZ.asp'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

# tabela do ettj
ettjDiv = soup.find('div',{'id':'ETTJs'})
table = ettjDiv.find('table',{'border':'1'})

# dia
dadosDiv = soup.find('div',{'id':'Dados'})
diaTh = dadosDiv.find('th')

tableHeaders = ['Vertices', 'ETTJ IPCA', 'ETTJ PRE', 'Inflacao Implicita', 'Data']

# removendo isso porcausa dos acentos, nao quero 
# importar uma lib nova so pra tirar unicode

#for x in table.find_all('th')[1:]:
#    title = x.text.strip()
#    table_headers.append(title)

tableData = []

for row in table.find_all('tr')[2:]:
    data = row.find_all('td')
    rowData = [td.text.strip() for td in data]
    rowData.append(diaTh.text)
    tableData.append(rowData)

#juntando os titulos com as info
resultado = [dict(zip(tableHeaders, t)) for t in tableData]

with open('table.json', 'w') as f:
    json.dump(resultado, f)
