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

# mostra o tipo da variável fins didáticos
# print(type(valor))

# dentro da variável valor podemos ver que existem diversos outros indicadores
# devemos extrair o indicador desejado

# pega e imprime o valor do BTC

precoBTC = re.findall(r'\$[0-9,.]+',valor.text)

# transforma precoBTC em string

# Mostra o tipo da variável precoBTC

# print(type(precoBTC))

# Transforma a lista em string
BTC = str(precoBTC)

# Mostra o tipo de variável

#print(type(BTC))

# Tratamento da string precoBTC para que a mesma vire float 
# primeiro remoção dos colchetes( [] ), depois cifrão ($), depois a vírgula(,) e por fim
# as aspas simples (') 

BTC = str(BTC).strip('[]')

BTC = BTC.replace('$',"")

BTC = BTC.replace(',',"")

BTC = BTC.strip("'")

#  transforma a string em float

teste = ast.literal_eval(BTC)


# Mostra o tipo da variável teste
#print(type(teste))

# imprime a variável teste

#print(teste)

# Variável BTC agora é to tipo float por receber a variável teste
BTC=teste


