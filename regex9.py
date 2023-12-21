"""
Expressões Regulares
-Múltiplas ocorrências - Método 'findall()':

* Enquanto search() retorna um objeto Match do primeiro texto 
correspondentena string pesquisada, o método findall() retorna 
as strings de todas as correspondências na string pesquisada. 
* Para ver como search() retorna umobjeto Match somente da primeira 
instância do texto correspondente, digite oseguinte no shell interativo:
>>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
>>> mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
>>> mo.group()
'415-555-9999'
* Por outro lado, findall() não retorna um objeto Match, mas uma lista de
strings – desde que não haja grupos na expressão regular. Cada string 
da lista é uma parte do texto pesquisado que correspondeu à expressão 
regular. Digite o seguinte no shell interativo:
>>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # não tem 
nenhum grupo
>>> phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
['415-555-9999', '212-555-0000']
* Se houver grupos na expressão regular, findall() retornará uma lista de
tuplas. Cada tupla representa uma correspondência identificada, e seus 
itens serão as strings correspondentes a cada grupo da regex. Para ver 
findall() em ação, digite o seguinte no shell interativo (observe que a 
expressão regular sendo compilada agora contém grupos entre parênteses):
>>> phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # tem 
grupos
>>> phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
[('415', '555', '9999'), ('212', '555', '0000')]


"""
import re
print("Exemplo_1: ")

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo_search = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
mo_findall = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')

print(f"mo_search = {mo_search.group()}")
print(f"mo_findall = {mo_findall}") 
# Sem grupos => Gera uma lista de strings cujos itens é uma parte do texto
# que correspondeu à expressão regular.
print(" ")
print("Exemplo_2: ")
phoneNumRegex2 = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
mo_search2 = phoneNumRegex2.search('Cell: 415-555-9999 Work: 212-555-0000')
mo_findall2 = phoneNumRegex2.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(f"mo_search2 = {mo_search2.group()}")
print(f"mo_findall2 = {mo_findall2}") 
# Com grupos => Gera uma lista de tuplas cujos itens serão 
# as strings correspondentes a cada grupo da regex.
print(" ")
print("Exemplo_3:")
numero_telefone = re.compile('\(\d{2}\) \d{5}-\d{4}')
mo3 = numero_telefone.findall('Ligar para (88) 98765-1234 depois das 9h'+
'ou para (85) 97651-9834 apos às 12 horas')
print(f"mo3 = {mo3}")
print(f"mo3[0] = {mo3[0]}")
print(f"mo3[1] = {mo3[1]}")
print(" ")
print("Exemplo_4:")
numero_telefone = re.compile('(\(\d{2}\)) (\d{5}-\d{4})')
mo4 = numero_telefone.findall('Ligar para (88) 98765-1234 depois das 9h'+
'ou para (85) 97651-9834 apos às 12 horas')
print(f"mo4 = {mo4}")
print(f"mo4[0] = {mo4[0]}")
print(f"mo4[1] = {mo4[1]}")