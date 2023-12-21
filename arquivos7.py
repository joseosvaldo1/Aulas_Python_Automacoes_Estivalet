"""
Trabalhando com Arquivos (Parte VII):

* Lendo Arquivos de Texto:
- Se quiser ler todo o conteúdo de um arquivo como um valor de string, 
utilize o método read() do objeto File.  
- Passos para ler um arquivo de texto:
a) usar a função 'open(arquivo, mode)':
a1)Se 'arquivo' estiver no mesmo diretório onde o Python estiver rodando,
basta especificar o nome do arquivo. Caso contrário, deve-se utilizar 
o caminho absoluto (ou o caminho relativo) do 'arquivo'; 
a2)mode = 'r' (somente leitura - r=>read mode - modo padrão), 
'w' (escrita - w=> write mode) ou 'a' (adicionar - a=> append 
mode)

b) Ler o texto/arquivo:
b1) read() - Lê todo o texto do arquivo em uma única string;
b2) readline() - Lê linha por linha do arquivo retornando uma string 
por linha;
b3) readlines() - Lê todas as linhas do arquivo retornando uma lista de
strings (uma para cada linha).

c) Fechar o arquivo: Para liberar recursos no sistema operacional
c) close()
"""
import os
from pathlib import Path
print("Exemplo_1:")
# Usando o método 'read()':
path_1 = r'C:\Users\Usuário\Desktop\Osvaldo\Work Spaces\ws-python_estivalet\arquivos\soneto.txt'
with open(path_1,'r') as f1:
    contents_1 = f1.read()


print(contents_1)
f1.closed()
# Observação: Caso a saída conste com caracteres não lidos, deve-se
# utilizar o parãmetro encoding: 
# with open(path_1, encoding='utf8) as f1:
# Não é preciso passar o parâmetro 'r', pois ele é o padrão (default).
print(" ")
print("Exemplo_2:")
# Usando o método 'redeline()'
lines = []
with open(path_1) as f2: 
    lines = f2.readlines()


count = 0
for line in lines:
    count += 1
    print(f"line[{count}] = {line}")

f2.closed()
print(" ")
print("Exemplo_2:")
# Usando o método 'readlines()':
with open(path_1) as f3:
    line = f3.readline()
    while line:
        print(line)
        line = f3.readline()

f3.closed()