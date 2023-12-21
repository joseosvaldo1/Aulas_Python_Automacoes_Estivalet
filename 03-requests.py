"""
Web Scraping (Parte III):

- Biblioteca BeautifulSoup - parte II:
- Selecionando tags por classes e ids:

"""
from bs4 import BeautifulSoup as bs
import requests
url = "https://estivalet.github.io/static-testing-sites/simple/ids_classes.html"
reponse = requests.get(url)

print(f"Status Code: {reponse.status_code}")
print(30*"-")
print(" ")
html = reponse.content 
# O método 'content' acima retorna o conteúdo da página em html
# em uma única linha. 
print("HTML DA PAGINA:")
print(html)
print(30*"-")
print(" ")
soup = bs(reponse.content, "html.parser")
print("Imprimindo a lista de tags 'p':")
print(soup.find_all('p', class_='outer-text'))
print(30*"-")
print(" ")
print(soup.find_all('p', class_='outer-text'))
# O método 'find_all' retorna uma lista com todas as tags 'p' 
# que possuem a classe 'outer-text'. Se retirarmos o primeiro
# argumento de, o método retornará uma lista com todas 
# as tags que possuem a classe 'outer-text'. Podemos também, 
# especificar somente um determinado 'id'.
print(30*"-")
print(" ")
print("CLASS 'OUTER-TEXT':")
print(soup.find_all(class_='outer-text'))
print(" ")
print("CLASS 'INNER-TEXT':")
print(soup.find_all(class_='inner-text'))
print(30*"-")
print(" ")
print("ID 'FIRST':")
print(soup.find_all(id='first'))
print(" ")
print("ID 'SECOND':")
print(soup.find_all(id='second'))
print(30*"-")
print(" ")
print("PEGANDO TEXTOS DAS TAGS E IDS:")
print(soup.find_all(class_='outer-text')[0].get_text())
print(" ")
print(soup.find_all(id='first')[0].get_text())
print(" ")
# Para retirar os espaços em branco desnececessários, podemos
# utilizar o método 'strip':
print("PEGANDO TEXTOS DAS TAGS E IDS SEM ESPACOS EM BRANCO:")
print(soup.find_all(id='first')[0].get_text().strip())
print(" ")
print(soup.find_all(id='second')[0].get_text().strip()) 