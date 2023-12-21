"""
Web Scraping (Parte II):
-Biblioteca BeautifulSoup - parte I:
"""
from bs4 import BeautifulSoup as bs
import requests
url = "https://estivalet.github.io/static-testing-sites/simple/simple.html"
reponse = requests.get(url)

print(f"Status Code: {reponse.status_code}")
print(30*"-")
print(" ")
html = reponse.content 
# O método 'content' acima retorna o conteúdo da página em html
# em uma única linha. 

soup = bs(reponse.content, "html.parser")
print("Imprimindo a lista de tags 'p':")
print(soup.find_all('p')) 
# O método 'find_all' retorna uma lista com todas as tags 'p'
print(30*'-')
print(" ")
print(soup.find('p'))
# O método 'find' retorna a primeira ocorrência da tag 'p'
print(soup.find('p').get_text()) 
# O método 'get_text' retorna o texto de soup.find('p').
print(30*'-')
print(" ")