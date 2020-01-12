# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import xlrd

print("Iniciando nosso robô... \n")

dominios = []

#Lendo do Excel
workbook = xlrd.open_workbook('dominio.xlsx')
sheet = workbook.sheet_by_index(0)
for linha in range(0,8):
    dominios.append(sheet.cell_value(linha,0))

driver = webdriver.Chrome('/home/marcos/Projetos/robos/RobosAutomatico/chromedriver')
driver.get("https://registro.br/")

for dominio in dominios:
    pesquisa = driver.find_element_by_id("is-avail-field")
    pesquisa.clear() # Limpando Input de Pesquisa
    pesquisa.send_keys(dominio)
    pesquisa.send_keys(Keys.RETURN)
    time.sleep(2); #Dormi 2 s
    resultados = driver.find_elements_by_tag_name("strong")
    #import pdb; pdb.set_trace() Break pdb
    print("Dominio %s %s" % (dominio, resultados[4].text))

driver.close();