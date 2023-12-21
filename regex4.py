"""
Expressões Regularees (REGEX)
- Zero ou uma ocorrência: Podemos encontrar zero ou uma ocorrência em 
uma expressão regular utilizando o metacaracter ponto de interrogação.
(?)

"""
import re
print("Exemplo_1: ")
phone_number = re.compile('(\(\d{2}\) )?(\d{5}-\d{4})')
no1 = phone_number.search("Ligar para (71) 98756-1234 apos 9 horas da manha.")
print(f"no1 = {no1.group()}")
print(" ")
print("Exemplo_2: ")
phone_number = re.compile('(\(\d{2}\) )?(\d{5}-\d{4})')
# Grupos:                     Opicional?Obrigatório          

# O caractere ? marca o grupo que o antecede como sendo uma parte 
# opcional do padrão (zero ou uma ocorrência). 
no2 = phone_number.search("Ligar para 98756-1234 apos 9 horas da manha.")
print(f"no2 = {no2.group()}")
print(" ")
