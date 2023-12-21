"""
Expressões Regulares - Grupos:

Grupos: são formas de agrupar expressões. Com eles, podemos selecionar 
o que queremos ou não receber nos resultados. Até agora, estamos definindo 
expressões sem grupo e quando temos um match, é no resultado inteiro da 
expressão.

"""

import re
print("Exemplo_1: ")
phone_number = re.compile('(\(\d{2}\)) (\d{5}-\d{4})')
#Grupos:                         1            2    
result = phone_number.search('Meu numero e (21) 87657-1029. Ligar apos 19 horas.')
print(f"Resultado(s) econtrado(s) = {result.group()}")
print(f"DDD - grupo 1 = {result.group(1)}")
print(f"Telefone - grupo 2 = {result.group(2)}")
print(f"DDD + Telefone = {result.group(0)}")
print(" ")
print("Exemplo_2: ")
ddd, telefone = result.groups()     # atribuição múltipla em uma tupla
# result.groups[0] = '(21)'
# result.groups[1] = '87657-1029'
print(f'DDD = {ddd}')
print(f'Telefone = {telefone}')

