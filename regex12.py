"""
Expressões Regulares:

Padrões de Início e Fim:

- O símbolo de acento circunflexo (^) também pode ser usado no início de 
uma regex para indicar que uma correspondência deve ocorrer no início de 
um texto pesquisado. Da mesma maneira, podemos colocar um sinal de dólar 
($) no final da regex para indicar que a string deve terminar com esse 
padrão de regex. Além disso, podemos usar ^ e $ juntos para indicar que a 
string toda deve corresponder à regex – ou seja, não é suficiente que uma
correspondência seja feita com algum subconjunto da string.

- ^ => INÍCIO       $ => FIM

"""
import re
print("Exemplo_1:")
comeca_com_curso = re.compile('^Curso')
mo1 = comeca_com_curso.search('Curso de Python do Zero a Automacao')
print(f'mo1-detalhamento = {mo1}')
print(f'mo1 = {mo1.group()}')
print(" ")
print("Exemplo_2:")
termina_com_numero = re.compile('\d$')
mo2 = termina_com_numero.search('Seu numero e 76')
print(f'mo2-detalhamento = {mo2}')
print(f'mo2 = {mo2.group()}')
print(" ")
print("Exemplo_3:")
string_numerica = re.compile('^\d+$')
mo3 = string_numerica.search('3456279')
print(f'mo3-detalhamento = {mo3}')
print(f'mo3 = {mo3.group()}')
