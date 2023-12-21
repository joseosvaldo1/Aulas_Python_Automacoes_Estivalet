"""
Automação Web - Parte IX:

* Trabalhando Com Caixas de Seleção:

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


driver = webdriver.Chrome()
page = "https://estivalet.github.io/robot-static-testing-site/cadastro/index.html"
driver.get(page)

text = "Desenvolvido para o curso de automação com Robot Framework"

select_element = driver.find_element(By.ID, 'estado-civil')
select_object = Select(select_element)
time.sleep(3)
# select_object.select_by_index(4)
select_object.select_by_value('Casado(a)')
time.sleep(3)

"""
all_available_options = select_object.options
print(50*'-')
print("Elements Options:")

for option in all_available_options:
    print(option.text)
    
print(" ")
print(50*'-')
"""

driver.close()
