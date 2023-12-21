"""
Expressões Regulares (REGEX)

* Ignorando Caracteres Maiúsculos e Minúsculos:
- Para fazer sua regex ignorar as diferenças entre letras maiúsculas
e minúsculas (ser case-insensitive), re.IGNORECASE ou re.I pode ser
passado como segundo argumento de re.compile()

"""
import re
print("Exemplo_1:")
texto = re.compile('python',re.I)
mo1 = texto.search('Curso de Python do Zero a Automacao.')
mo2 = texto.search('Curso de PYTHON do Zero a Automacao.')
mo3 = texto.search('Curso de python do Zero a Automacao.')
print(f'mo1 = {mo1.group()}')
print(f'mo2 = {mo2.group()}')
print(f'mo3 = {mo3.group()}')
print(" ")

