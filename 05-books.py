"""
Web Scraping (Parte V):

- Scraping de Dados de Uma Livraria On Line:
* url: https://estivalet.github.io/static-testing-sites/bookdepository

"""
from bs4 import BeautifulSoup as bs
import requests
import sys

# Definir o encoding padrão para utf-8
sys.stdout.reconfigure(encoding='utf-8')

url = "https://estivalet.github.io/static-testing-sites/bookdepository"
reponse = requests.get(url)
html = reponse.content
soup = bs(html, "lxml") # lxml é o parser mais rápido

# Pegando o título do livro:
all_h3 = soup.find_all('h3', class_='title')
# Imprimindo os títulos dos livros:
print("TITULOS DOS LIVROS:")
for h3 in all_h3:
    print(h3.get_text().strip())

print(30*"-")
print(" ")
# Pegando todos os itens dos livros da página:
book_items = soup.find_all('div', class_='book-item')
# Imprimindo os títulos dos livros:
print(27*'-')
print("INFORMAÇÕES DE CADA LIVRO:")
print(27*'-')
print(" ")
for book_item in book_items:
    print("Title: " + book_item.find('h3').get_text(strip=True))
    print("Author: " + book_item.find('p', class_='author').get_text(strip=True))
    print("Published on: " + book_item.find('p', class_='published').get_text(strip=True))
    print("Formate: " + book_item.find('p', class_='format').get_text(strip=True))
    original_price = book_item.find('span', class_='rrp')
    current_price = book_item.find('p', class_='price')
    if not current_price:
        preco = print("Price: Out Of Stock")
    else:
        if original_price:
            print('Preço Original: ' + original_price.get_text(strip=True))
            print('Preço Atual: R' + current_price.get_text(strip=True).split('R$')[0])
        else:
            print('Preço: R' + current_price.get_text(strip=True))
    print(30*'-' + '\n  ')

