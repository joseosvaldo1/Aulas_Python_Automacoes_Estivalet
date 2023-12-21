"""
Web Scraping (Parte I):

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
soup.find_all("p")


print(soup.prettify())
print(html)
# Utilizando 'bs(response.content,"html.parser")' e o método
# 'prettify' acima retorna o conteúdo da página em html de 
# forma estruturada, ou seja, com as tags html, head, body, 
# etc.
print(30*"-")
print(" ")
print(soup.children)
print("Itens:")
for item in list(soup.children):
    print(item)

print(30*"-")
print(" ")
print("Tipos de Itens:")
for item in list(soup.children):
    print(type(item))

print(30*"-")
print(" ")
html = list(soup.children)[2]
body = list(html.children)[3]
print(30*"-")
print(" ")
print(list(body.children))
p = list(body.children)[1]
print(30*"-")
print(" ")
print(p)
print(" ")
print(p.get_text())


