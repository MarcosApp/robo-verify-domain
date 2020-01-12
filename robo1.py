# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print("Iniciando nosso robô... \n")

driver = webdriver.Chrome('/home/marcos/Projetos/robos/RobosAutomatico/chromedriver')
driver.get("https://registro.br/")

dominios = ["roboscompython.com.br", "udemy.com.br", "uol.com.br"]

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