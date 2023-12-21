"""
Expressões Regulares:

* Caracteres ponto (.) e asterico (*):
- O caractere . (ou ponto) em uma expressão regular é chamado de 
caractere-curinga e corresponde a qualquer caractere, exceto uma 
quebra de linha.
- Podemos usar ponto-asterisco (.*) para indicar “qualquer caractere”. 
Lembre-se de que o caractere ponto quer dizer “qualquer caractere único, 
exceto a quebra de linha” e o caractere asterisco quer dizer “zero ou 
mais ocorrências do caractere anterior” 

"""
import re
print("Exemplo_1:")
ato_regex = re.compile('.ato')
mo1 = ato_regex.findall('O gato entrou no mato e encontrou um rato' + 
                        'dentro do jatoba.')
print(f'mo1={mo1}')
print(" ")
print("Exemplo_2:")
nome_regex = re.compile('Primeiro Nome: (.*) Sobrenome: (.*)')
mo2 = nome_regex.search('Primeiro Nome: Jose Sobrenome: da Silva')
print(f"mo2-detalhamento = {mo2}")
print(f"mo2-grupos = {mo2.groups()}") # Gerou uma tupla com os match objects
print(f"mo2-grupo = {mo2.group()}") # Só mostrou os grupos de match objects
print(f"mo2-grupo(0) = {mo2.group(0)}")
print(f"mo2-grupo(1) = {mo2.group(1)}")
print(f"mo2-grupo(2) = {mo2.group(2)}")