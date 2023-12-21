"""
Automação Web - Parte II:

*Automatizando Pesquisa do Google com Selenium:

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(0.5)
driver.get("https://www.google.com.br/")

assert "Google" in driver.title

search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('Selenium')

search_button = driver.find_element(By.NAME, 'btnK')
search_button.click()

time.sleep(5)
driver.quit()
