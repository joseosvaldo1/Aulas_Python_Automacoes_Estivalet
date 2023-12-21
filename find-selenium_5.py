"""
Automação Web - Parte VII:

* Usando CSS Selectors Para Encontrar Elementos:

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
page = "https://estivalet.github.io/robot-static-testing-site/admin/index.html"
driver.get(page)

text = "Desenvolvido para o curso de automação com Robot Framework"
#element = driver.find_element(By.CSS_SELECTOR, "#content > div > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div.card-body > p")
element = driver.find_element(By.CSS_SELECTOR, "div.card-body > p")


print(50*'-')
print("Element:")
print(element)
print(" ")
print(50*'-')
print(f"element_name.text = {element.text}")
driver.close()
