"""
Métodos Úteis Das Strings - Parte II:

1) Método 'strip()': Este método retorna uma nova strip sem 
espaços em brancos no início ou no final da string.

help(str.strip) - strip(self, chars=None, /): Return a copy of the string with 
leading and trailing whitespace removed.If chars is given and not None, remove 
characters in chars instead.(Tradução:Retorne uma cópia da string com
espaços em branco iniciais e finais removidos. Se chars for fornecido e não 
None, removacaracteres em caracteres em vez disso.)

2) Método 'lstrip()': Este método retorna uma nova strip sem 
espaços em brancos no início (á esquerda) da string (left).

help(str.lstrip) - lstrip(self, chars=None, /): Return a copy of the string with 
leading whitespace removed.If chars is given and not None, remove characters 
in chars instead. (Tradução: Retorne uma cópia da string com
espaços em branco à esquerda removidos. Se caracteres forem fornecidos e não 
Nenhum, remova os caracteres em caracteres em vez disso.)

3) Método 'rstrip()': Este método retorna uma nova strip sem 
espaços em brancos no fim (á direita) da string (right).

help(str.rtrisp)-rstrip(self, chars=None, /): Return a copy of the string with 
trailing whitespace removed.If chars is given and not None, remove characters 
in chars instead.(Tradução: Retorne uma cópia da string com espaços em branco 
à direita removidos. Se os caracteres forem fornecidos e não nenhum, 
remova os caracteres em caracteres em vez disso.)

4) Método 'rjust()': Retorna uma string de largura de comprimento justificada 
à direita. O preenchimento é feito usando o caractere de preenchimento 
especificado (o padrão é um espaço em branco). 
- rjust(self, width, fillchar=' ', /)

5) Método 'ljust()': Retorna uma string de comprimento e largura justificada 
à esquerda. O preenchimento é feito usando o caractere de preenchimento 
especificado (o padrão é um espaço em branco).
- ljust(self, width, fillchar=' ', /)

6) Método 'center()': Retorna uma string centralizada de largura de 
comprimento. O preenchimento é feito usando o caractere de preenchimento 
especificado (o padrão é um espaço em branco).
- center(self, width, fillchar=' ', /)

"""
import pyperclip

print("Exemplo_1:")
string1 = "   Hello, world!     "
string2 = string1.strip()
string3 = string1.rstrip()
string4 = string1.lstrip()
print(f"string1 = {string1}")
print(f"string2 - strip() = {string2}")
print(f"string3 - rstrip() = {string3}")
print(f"string4 - lstrip() = {string4}")
print(" ")
print("Exemplo_2:")
text = pyperclip.paste()
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* '+lines[i]

text ='\n'.join(lines)
pyperclip.copy(text)
print(text)
# print(pyperclip.paste())
print(" ")
print("Exemplo_3: ")
string5 = 'Hello' # string5 já tem 5 caracteres
string6 = string5.rjust(11)
# rjust completa os 11 caracteres com mais 6 à direita da string5 espaços 
# em branco para totalizar 11 (5 da string5 e 6 espaços em brancos). 
string7 = string5.center(11) 
# center completa os 11 caracteres com 3 caracteres em branco à esquerda e 3 
# à direita da string5 que já possui 5 caracteres (5 da string5 e 6 espaços 
# em brancos).
string8 = string5.ljust(11)
# rjust completa os 11 caracteres com mais 6 à esquerda da string5 espaços 
# em branco para totalizar 11 (5 da string5 e 6 espaços em brancos)..
print(f"string6 - rjust = {string6}")
print(f"string7 - center = {string7}")
print(f"string8 - ljust  = {string8}")
print(" ")
print("Exemplo_4: ")
string9 = string5.rjust(11, '*')
string10 = string5.center(11, '*') 
string11 = string5.ljust(11, '*')
print(f"string9 - rjust   = {string9}")
print(f"string10 - center = {string10}")
print(f"string11 - ljust  = {string11}")
print(" ")
print("Exemplo_5: ")
compras = {'refrigerantes': 4, 'macas': 12, 'laranjas': 400, 'bananas': 12}
def list_print(dict_items, larg_col_esq, larg_col_dir):
    print('LISTA DE COMPRAS'.center(larg_col_esq + larg_col_dir,'-'))
    for k, v in dict_items.items():
        print(k.ljust(larg_col_esq, '.') + str(v).rjust(larg_col_dir))

list_print(compras, 20, 6)
