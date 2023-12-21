"""
Expressões Regulares:
- Múltiplos grupos:
O caractere | é chamado de pipe. Podemos usá-lo em qualquer lugar em
que quisermos fazer a correspondência de uma entre várias expressões.
Por exemplo, a expressão regular r'Batman|Tina Fey' corresponde a 'Batman' 
ou a'Tina Fey'.
Quando tanto Batman quanto Tina Fey ocorrerem na string pesquisada, a
primeira ocorrência do texto correspondente será retornada como o 
objeto Match.

"""
import re
print("Exemplo_1: ")
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(f"mo1 = {mo1.group()}")
print(" ")
print("Exemplo_2:")
regex = re.compile("Python|Automacao")
mo2 = regex.search("Curso de Python do Zero a Automacao")
mo3 = regex.search("Curso de Automacao")
print(f"mo2 = {mo2.group()}")
print(f"mo3 = {mo3.group()}")
print(" ")
print("Exemplo_3: ")
emails = re.compile("jose@(gmail|yahoo.com|apple.com)")
mo4 = emails.search("Mande um e-mail para jose@yahoo.com")
print(f"mo4 = {mo4.group()}")
print(f"mo4 = {mo4.group(1)}")