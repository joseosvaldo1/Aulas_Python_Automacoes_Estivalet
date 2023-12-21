"""
Automação Web - Parte V:

* Encontrando Tags:

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
page = "https://estivalet.github.io/robot-static-testing-site/admin/index.html"
driver.get(page)

text = "Desenvolvido para o curso de automação com Robot Framework"
element = driver.find_element(By.TAG_NAME, "h1")


print(50*'-')
print("Element:")
print(element)
print(" ")
print(50*'-')
print(f"element_name.text = {element.text}")
print(" ")
driver.close()
