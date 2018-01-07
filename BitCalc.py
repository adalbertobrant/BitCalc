# -*- coding: utf-8 -*-

## Calculadora de BitCoin 
### Importação através de scrapping do site Coingecko e do site Dolar Nubank

#  importação da bibliotecas

import os
import sys
import ast
import re
import requests
from bs4 import BeautifulSoup

# Faz a captura da página para a variável 'pagina'

pagina = requests.get('https://www.coingecko.com/en/coins/bitcoin')

# Obejeto do BeautifulSoup 

soup = BeautifulSoup(pagina.text, 'html.parser')

# Extrai do site da informação desejada nesse caso o valor do BitCoin no dia
# 

valor = soup.find(class_='coin-value')

# imprime a variável valor 

print(type(valor))

# dentro da variável valor podemos ver que existem diversos outros indicadores
# devemos extrair o indicador desejado

# pega e imprime o valor do BTC

precoBTC = re.findall(r'\$[0-9,.]+',valor.text)

# transforma precoBTC em string

print(type(precoBTC))



BTC = str(precoBTC)

print(type(BTC))

#BTC = str(precoBTC).strip('[]')

BTC = str(BTC).strip('[]')

BTC = BTC.replace('$',"")

BTC = BTC.replace(',',"")

BTC = BTC.strip("'")

teste = ast.literal_eval(BTC)

print(type(teste))

print(teste)
