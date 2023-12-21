"""
Web Scraping (Parte IV):

- Seletores CSS:

Exemplos:
1) p a => encontra todas as tags 'a' dentro de tags 'p'
2) body p a => encontra todas as tags 'a' dentro de tags 'p' 
dentro de tags 'body'
3) p.outer-text => encontra todas as tags 'p' com a classe 
'outer-text'
4) p#first => encontra todas as tags 'p' com o id 'first'
5) body p.outer-text => encontra todas as tags 'p' com a 
classe 'outer-text' dentro de tags 'body'

"""
from bs4 import BeautifulSoup as bs
import requests
import sys

# Definir o encoding padrão para utf-8
sys.stdout.reconfigure(encoding='utf-8')

url = "https://estivalet.github.io/static-testing-sites/simple/ids_classes.html"
reponse = requests.get(url)

print(f"Status Code: {reponse.status_code}")
print(30*"-")
print(" ")
html = reponse.content 
# O método 'content' acima retorna o conteúdo da página em html
# em uma única linha. 
print("HTML DA PÁGINA:")
print(html)
print(30*"-")
print(" ")
soup = bs(reponse.content, "html.parser")
print("Imprimindo a lista de tags 'p' dentro de div:")
print(soup.find_all('p', class_='outer-text'))
print(soup.select('div p'))
print(30*"-")
print(" ")