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

pagina = requests.get('http://economia.awesomeapi.com.br/BTC-BRL/1?format=xml')
dolarReal = requests.get('http://economia.awesomeapi.com.br/USD-BRL/1?format=xml')



# Obejeto do BeautifulSoup 

soup = BeautifulSoup(pagina.text, 'html.parser')
soup1 = BeautifulSoup(dolarReal.text,'html.parser')



# Imprime Soup1 comando prettify()

#print(soup1.prettify())

#print(list(soup1.children))


# Extrai do site da informação desejada nesse caso o valor do BitCoin no dia
# 

valor = soup.find_all('high')
vdolarReal = soup1.find_all('high')

# imprime a variável valor 

# mostra o tipo da variável fins didáticos
#print(type(vdolarReal))

# dentro da variável valor podemos ver que existem diversos outros indicadores
# devemos extrair o indicador desejado

# pega e imprime o valor do BTC

#precoBTC = re.findall(r'\$[0-9,.]+',valor.text)

# transforma precoBTC em string

# Mostra o tipo da variável precoBTC

# print(type(precoBTC))

# Transforma a lista em string
BTC = str(valor)
Dolar = str(vdolarReal)


# Mostra o tipo de variável

#print(type(BTC))

# Tratamento da string precoBTC para que a mesma vire float 
# primeiro remoção dos colchetes( [] ), depois cifrão ($), depois a vírgula(,) e por fim
# as aspas simples (') 



Dolar = str(Dolar).strip('[]')

Dolar = str(Dolar).strip('<high>')

Dolar = str(Dolar).strip('</')

BTC = str(BTC).strip('[]')
BTC = str(BTC).strip('<high>')
BTC = str(BTC).strip('</')


#  transforma a string em float

teste = ast.literal_eval(BTC)
teste1 = ast.literal_eval(Dolar)


# Mostra o tipo da variável teste
#print(type(teste))

# imprime a variável teste

#print(teste)

# Variável BTC e Dolar  agora é to tipo float por receber a variável teste
BTC = teste
Dolar = teste1

print (" \nPrograma para o Cálculo do Valor de Bitcoin em Dolar do dia\n ")

print (" 1 BTC Vale = R$",BTC," reais")

print (" 1 Dolar Comercial Vale = R$ ",Dolar,"\n")

usrBTC = input("Entre com o valor desejado em BTC = ")

usrBTC = float(usrBTC)

calculo = usrBTC * BTC

print(" \nO valor em reais é = R$  ",calculo)
