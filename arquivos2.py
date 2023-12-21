"""
Arquivos - Parte II

* Função 'Path()':

- Todo programa executado em seu computador tem um diretório de trabalho
atual (current working directory, ou cwd). Supõe-se que qualquer nome de
arquivo ou path que não comece com a pasta-raiz esteja no diretório de
trabalho atual. Podemos obter o diretório de trabalho atual como um valor 
de string usando a função os.getcwd() e alterá-lo com os.chdir().

"""

from pathlib import Path

print("Exemplo_1:")
# Usando a função somente a função Path(): 
windows_path1 = Path('aulas','python','modulo1') # \ => Windows 
windows_path2 = str(Path('aulas','python','modulo1')).replace('\\','/') 
# / => Linux e Mac
print(f"windows_path1 = {windows_path1}")
print(f"windows_path2 = {windows_path2}")
print(" ")
print("Exemplo_2:")
# Usando a concatenação e Path():
windows_path3 = Path('aulas') / 'python' / 'modulo1'
windows_path4 = 'aulas' / Path('python') / 'modulo1'
# windows_path5 = 'aulas' / 'python' / Path('modulo1') => Erro
# Observação: A barra deve sempre estar relacionada a função Path

print(f"windows_path3 = {windows_path3}")
print(f"windows_path4 = {windows_path4}")
print(" ")
print("Exemplo_3:")
import os
from pathlib import Path
wd = windows_path1 = Path.cwd() 
# wd => working directory = diretório de trabalho atual
print(f"working directory1 = {wd}")
os.chdir('C:\\Windows\\System32')
print(f"working directory2 = {wd}") 
# Obs: Só funciona no terminal interativo do Python
print(" ")
print("Exemplo_3:")
# Determinando o diretório p
home = Path.home()
print(f"home = {(home)}")





