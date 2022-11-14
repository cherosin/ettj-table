import requests
import json
from bs4 import BeautifulSoup

url = 'https://www.anbima.com.br/informacoes/est-termo/CZ.asp'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

ettjDiv = soup.find('div',{'id':'ETTJs'})
table = ettjDiv.find('table',{'border':'1'})

dadosDiv = soup.find('div',{'id':'Dados'})
diaTh = dadosDiv.find('th')

tableHeaders = ['Vertices', 'ETTJ IPCA', 'ETTJ PRE', 'Inflacao Implicita']
tableData = []

for row in table.find_all('tr')[2:]:
    data = row.find_all('td')
    rowData = [td.text.strip() for td in data]
    tableData.append(rowData) 

resultado = [dict(zip(tableHeaders, t)) for t in tableData]

titulos = ['tax', 'value', 'date']
informacoes = []

for x in resultado:
    informacoes.append(['ETTJ IPCA', x['ETTJ IPCA'], diaTh.text + ' + ' + x['Vertices']])

resultadoFinal = [dict(zip(titulos, t)) for t in informacoes]

with open('table.json', 'w') as f:
    json.dump(resultadoFinal, f)
    