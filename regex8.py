"""
Expressões Regulares (REGEX):

- Ocorrências específicas:

- Se temos um grupo que se repete um número específico de vezes, basta 
usarmos a sintaxe de abre e fecha chaves-{}- para indicar o número de 
repetições.

- Se você tiver um grupo que deseja repetir um número específico de vezes,
insira um número entre chaves após o grupo em sua regex. Por exemplo, a
regex (Ha){3} corresponde à string 'HaHaHa', mas não a 
'HaHa', pois essa última tem apenas duas repetições do grupo (Ha).

# Faixa de valores:
- Em vez de um número, podemos especificar um intervalo especificando um
mínimo, uma vírgula e um máximo entre chaves. Por exemplo, a regex (Ha)
{3,5} corresponde a 'HaHaHa', 'HaHaHaHa' e 'HaHaHaHaHa'.
('Python'){2,4} => Duas, três ou quatro repetições da string 'Python'
('Python'){3,} => Três ou mais repetições da string 'Python'
('Python'){,5} => De zero até 5 repetições da string 'Python'

# Quantificadores 'gulosos' (greedy) e não-gulosos/preguiçosos (nongreedy):
- Quantificador guloso (greedy): Em situações ambíguas, sempre retorna a 
maior string possível.

- Quantificador preguiçoso/não-goloso (nongreedy): Em situações ambíguas, 
sempre retorna a menor string possível.

Observação: As expressões regulares em Python são greedy (gulosas) por default, 
o que significa que, em situações ambíguas, a correspondência será feita com a
maior string possível. Na versão nongreedy (não gulosa) das chaves, que faz a
correspondência com a menor string possível, um ponto de interrogação é
usado depois da chave de fechamento.

"""

import re
print("Exemplo_1:")
gulosa = re.compile('(Python){2,4}')
mo1 = gulosa.search("PythonPythonPythonPython")
print(f"mo1 = {mo1.group()}")
print(" ")
print("Exemplo_2:")
preguicosa = re.compile('(Python){2,4}?')
mo2 = preguicosa.search("PythonPythonPythonPython")
print(f"mo2 = {mo2.group()}")
