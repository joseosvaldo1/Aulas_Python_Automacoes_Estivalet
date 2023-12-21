"""
Automação Web - Parte III:

* Pesquisando elemtos por ID, NAME e XPATH:

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
page = "https://estivalet.github.io/robot-static-testing-site/"
driver.get(page)

element_id = driver.find_element(By.ID, 'username')
element_name = driver.find_element(By.NAME, 'password')

# Full xPATH => '/html/body/div/div/div/div[2]/form/div[3]/div/a'
# xPATH => '//*[@id="login"]'

#element_xpath = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/form/div[3]/div/a')
element_xpath = driver.find_element(By.XPATH,'//*[@id="login"]') 
print(f"element_id = {element_id}")
print(50*'-')
print(f"element_name = {element_name}")
print(50*'-')
print(f"element_xpath = {element_xpath}")
print(50*'-')

driver.close()
