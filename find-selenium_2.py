"""
Automação Web - Parte IV:

* Encontrando Elementos com Links:

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sys

# Definir o encoding padrão para utf-8:
sys.stdout.reconfigure(encoding='utf-8')

driver = webdriver.Chrome()
page = "https://estivalet.github.io/robot-static-testing-site/cadastro/index.html"
driver.get(page)

text = "Desenvolvido para o curso de automação com Robot Framework"
element = driver.find_element(By.LINK_TEXT, text)
partial_element = driver.find_element(By.PARTIAL_LINK_TEXT, "automação")

print(50*'-')
print("Element:")
print(element)
print(" ")
print(f"element_name.text = {element.text}")
print(50*'-')
print("Partial Element:")
print(partial_element)
print(" ")
print(f"partial_element_name.text = {partial_element.text}")
driver.close()
