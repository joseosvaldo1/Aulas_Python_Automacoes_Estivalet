"""
Automação Web - Parte I:


"""

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com.br/")
time.sleep(5)
driver.quit()
