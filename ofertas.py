#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import re
from bs4 import BeautifulSoup

# Remove HTML tags
def removeTags(data):
    rData = data.get_text()
    review_text = BeautifulSoup(rData)
    return review_text.get_text()

# Return category slug
def getChoice(option):
    slug = ["uam","ual","uca","uco","ugr","uhu","ujaen","uma","us","upo","upct"]
    if option<1 or option>11: option = 1
    return slug[option-1]

# Show menu
print ("""
OFERTAS POR PROGRAMA - PLATAFORMA ICARO

    1. Universidad Autónoma de Madrid
    2. Universidad de Almería
    3. Universidad de Cádiz
    4. Universidad de Córdoba
    5. Universidad de Granada
    6. Universidad de Huelva
    7. Universidad de Jaén
    8. Universidad de Málaga
    9. Universidad de Sevilla
    10. Universidad Pablo de Olavide
    11. Universidad Politécnica de Cartagena

    """)

opt = getChoice(int(input("Seleccione una categoría [1-11]: ")))

# Concatenate URL base with category and to do request
url = 'https://icaro.ual.es/'+opt
resp = urllib.request.urlopen(url)
respData = resp.read()

parsed_html = BeautifulSoup(respData,'html.parser')
jobs = parsed_html.select("div.cluster_capsule")

# Iterate jobs with clear format
for item in jobs:
    print("Programa: "+removeTags(item.select("dd")[1]))
    print("Fecha de Inicio: "+removeTags(item.select("dd")[3]))
    print("Duración: "+removeTags(item.select("dd")[4]))
    print("Descripción: "+removeTags(item.select("dd")[5]))
    print("https://icaro.ual.es"+item.a.get('href'))
    print("--------------------------------------------------------------------")

resp.close()