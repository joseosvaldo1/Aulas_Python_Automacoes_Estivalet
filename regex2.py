""" 
Expressões Regulares (Regex)
- Encontrando padrões com expressões regulares:
- Regex: São descrições para um padrão de texto.
- \d - representa um dígito (de 0 a 9)
- \d\d\d\d\d-\d\d\d\d => \d{5}-\d{4}
- \d{n} - \d n vezes
- Todas as funções para expressões regulares no 
Python estão contidas num módulo chamado 're'
"""
import re
print("Exemplo_1: ")
phone_number = re.compile(r'\d\d\d\d\d-\d\d\d\d')

result1 = phone_number.search('Meu numero eh 33497-3797.')
result2 = phone_number.search('Meu numero eh 33497 3797.')

print(f"result1 = {result1}") 
print(f"result2 = {result2}")
# O método 'seacrh()' retornará um objeto 'match' caso encontre o padrão.
#Caso contrário, ele retornará 'None'.
result3 = phone_number.search('Meu numero eh 87657-1029. Ligar apos 19 horas.')
result4 = result3.group()

print(f"telefone(s) encontrado(s): {result4}")
print("telefone(s) encontrado(s): " + result4)
# Ao resultado do método 'search()', aplica-se o método 'group()' para
# agrupar os padrões encontrados.
print(" ")
print("Exemplo_2: ")
phone_number2 = re.compile(r'\d{5}-\d{4}')
result5 = phone_number2.search('Meu numero eh 98930-9650. Ligar apos 19 horas.')
result6 = result5.group()
print(f"telefone(s) encontrado(s): {result6}")
print("telefone(s) encontrado(s): " + result6)
print(" ")
print("Exemplo_3: ")
phone_number2 = re.compile(r'\(\d{2}\) \d{5}-\d{4}')
result7 = phone_number2.search('Meu numero eh (85) 98930-9650. Ligar apos 19 horas.')
result8 = result7.group()
print(f"telefone(s) encontrado(s): {result8}")
print("telefone(s) encontrado(s): " + result8)
print(" ")