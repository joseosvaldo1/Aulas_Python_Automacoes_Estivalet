"""
Trabalhando com Arquivos:
Criando Pastas (Parte IV):

- os.makedirs(name: StrOrBytesPath, mode: int = 511, exist_ok: bool = False) 
-> None makedirs(name [, mode=0o777][, exist_ok=False])

Super-mkdir; create a leaf directory and all intermediate ones. 
Works like mkdir, except that any intermediate path segment (not 
just the rightmost) will be created if it does not exist. If the 
target directory already exists, raise an OSError if exist_ok 
is False. Otherwise no exception is raised. This is recursive.

Path(path).mkdir: Create a new directory at this given path. 
(method) 
def mkdir(
    mode: int = 511,
    parents: bool = False,
    exist_ok: bool = False
) -> None


"""
import os
from pathlib import Path

print("Exemplo_1: ")
path = 'C:\Temp' #Caminho da pasta onde serão criadas outras pastas 
path_1 = 'C:\Temp\Python3\modulo_01'
new_dir_1 = os.makedirs(path_1, exist_ok=True)
print(f"new_dir_1= {os.path.abspath(path_1)}") 
print(" ")
print("Exemplo_2:")
path_2 = 'C:\Temp\Python3\modulo_02'
os.chdir(path)
new_dir_2 = Path(path_2).mkdir(exist_ok=True)
print(f"new_dir_2= {os.path.abspath(path_2)}") 
print(" ")
print("Exemplo_3")
path_3 = 'C:\Temp\Python3\modulo_03'
new_dir_:3 = Path(path_3).mkdir(parents=True, exist_ok=True)
print(f"new_dir_3= {os.path.abspath(path_3)}") 
print(" ")