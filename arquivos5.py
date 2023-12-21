"""
Trabalhando com Arquivos (Parte V):

* Listando Arquivos:

# Obtendo os tamanhos dos arquivos e o conteúdo das pastas:

- Após ter dominado as maneiras de lidar com paths de arquivo, você poderá
começar a reunir informações sobre arquivos e pastas específicos. O módulo
os.path disponibiliza funções para obter o tamanho de um arquivo em bytes e
os arquivos e as pastas que estiverem em uma determinada pasta.

a)  Chamar os.path.getsize(path) retornará o tamanho em bytes do arquivo no
argumento path.
b) Chamar os.listdir(path) retornará uma lista de strings com nomes de 
arquivo para cada arquivo no argumento path. (Observe que essa função está 
no módulo os, e não em os.path.)

"""
import os
from pathlib import Path

print("Exemplo_1:")
# Determinando os componentes de uma pasta em uma lista: 
path_1 = r'C:\Users\Usuário\Desktop\Osvaldo\Work Spaces'
file_list_1 = os.listdir(path_1)
print(f"file_list_1 = {file_list_1}")
print(" ")
print("Exemplo_2:")
# Determinando o tamanho total de dado arquivo.
path_2 = r'C:\Users\Usuário\Desktop\Osvaldo\Atividade do Percurso Gerativo do Sentido.pdf'
file_size_1 = os.path.getsize(path_2)
print(f"file_size_1  = {file_size_1 }")
print(" ")
print("Exemplo_3:")
# Determinando o tamanho total somente dos arquivos de uma pasta:
total_size = 0
path_3 = r'C:\Users\Usuário\Desktop\Osvaldo'
for file_name in os.listdir(path_3):
    total_size += os.path.getsize(Path(path_3) / file_name)

print(f'total_size = {total_size}')
print(" ")
print()
print("Exemplo_4:")
# Usando o método 'glob()' para achar os arquivos segundo um dado padrão:
po1 = Path(path_3) # po = Path Object
total_size_2 = 0
for file_name in po1.glob('*.pdf'):
    print(file_name)
    total_size_2 = total_size_2 + os.path.getsize(Path(path_3)/file_name)

print(f"total_size_2 dos *.pdf = {total_size_2}")
