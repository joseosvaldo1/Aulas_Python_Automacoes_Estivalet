"""
Automação Web - Parte VIII:

* Encontrando Múltiplos Elementos:

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
page = "https://estivalet.github.io/robot-static-testing-site/admin/index.html"
driver.get(page)

text = "Desenvolvido para o curso de automação com Robot Framework"

elements = driver.find_elements(By.XPATH, '//li[@class="nav-item"]')
# elements = driver.find_elements(By.CLASS_NAME, 'nav-item')
# elements = driver.find_elements(By.CSS_SELECTOR, 'li.nav-item span')

# Observação: o método find_elements() retorna uma lista (array) de 
# elementos, enquanto o método find_element() retorna apenas um 
# elemento.


print(50*'-')
print("Elements:")
print(elements)
print(" ")
print(50*'-')
print("Elements Text:")
for element in elements:
    print(element.text)

print(" ")
print(50*'-')

