"""
Expressões Regulares (REGEX):

Zero ou Mais Ocorrências(*):
- O asterisco (*) quer dizer 'corresponda a zero ou mais', ou seja, o grupo
que antecede o asterisco pode ocorrer qualquer número de vezes no texto. 
Esse grupo poderá estar totalmente ausente ou ser repetido diversas vezes.

"""
import re
print("Exemplo_1:")
zero_ou_mais = re.compile('Pytho*n')
mo1 = zero_ou_mais.search("Curso de Python")
mo2 = zero_ou_mais.search("Curso de Pythooooooooon")
mo3 = zero_ou_mais.search("Curso de Pythn")
print(f"mo1 = {mo1.group()}")
print(f"mo2 = {mo2.group()}")
print(f"mo3 = {mo3.group()}")
