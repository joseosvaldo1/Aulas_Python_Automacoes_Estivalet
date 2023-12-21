"""
Trabalhando Com Arquivos - Parte IV:

* Criando Pastas 

- Seus programas podem criar novas pastas (diretórios) com a função
os.makedirs().

- A função os.makedirs() do módulo os.path do Python é utilizada para 
criar diretórios recursivamente. 

# Uso da função 
import os

os.makedirs(path, mode=0o777, exist_ok=False)

# path: O caminho do diretório que você deseja criar, incluindo todos os 
diretórios pais necessários. Pode ser uma string ou um objeto de caminho 
(path-like object).

# mode (opcional): As permissões do diretório que está sendo criado. O 
valor padrão é 0o777, que atribui permissões máximas de leitura, gravação 
e execução para o proprietário, grupo e outros usuários. 

# exist_ok (opcional): Se definido como True, não ocorrerá nenhum 
erro se o diretório já existir. O valor padrão é False, o que significa 
que será lançada uma exceção FileExistsError se o diretório já existir.

- A função os.mkdir() do módulo os do Python é usada para criar um 
diretório no caminho especificado. Ao contrário da função os.makedirs(), 
a função os.mkdir() não cria diretórios pais automaticamente. Portanto, 
o diretório pai deve existir antes de chamar essa função.

# Forma de Uso:

import os

os.mkdir(path, mode=0o777) 

# path: O caminho do diretório que você deseja criar.

# mode (opcional): As permissões do diretório que está sendo criado. 
O valor padrão é 0o777, que atribui permissões máximas de leitura, 
gravação e execução para o proprietário, grupo e outros usuários.


"""
import os
from pathlib import Path

print("Exemplo_1:")
path1 = 'C:\Temp'
path2 = 'C:\Temp\python\modulo1'
new_dir1 = os.path.exists(path2)

if os.path.exists(path2):
    print(f'os.path.exists(path2) = {os.path.exists(path2)}')
else:
    try:
        os.makedirs(path1)
        print("A pasta 'C:\Temp\python\modulo1' foi criada com sucesso!")
    except: FileExistsError
    print("Nao e possivel criar uma pasta ja existente!")

print(" ")
print("Exemplo_2:")
path3 = 'C:\Temp\python\modulo2'

# new_dir3 = os.mkdir(path3)
# ou Path(path3).mkdir()

new_dir3_exists = os.path.exists(path3)
# print(f'new_dir3_exists(path3) = {new_dir3_exists }')
print(" ")
if new_dir3_exists:
    print(f"new_dir3_exists = {new_dir3_exists}")
else:  
    try:   
        Path(path3).mkdir()
    except: FileExistsError
    print("Nao e possivel criar uma pasta ja existente!") 
print(" ")
print("Exemplo_3:")
path4 = 'C:\Temp\python\modulo3'
#new_dir4 = Path(path4).mkdir(parents=True)
new_dir4_exists = os.path.exists(path4)
# print(f'new_dir4_exists(path4) = {new_dir4_exists }')

if new_dir3_exists:
    print(f"new_dir4_exists = {new_dir4_exists}")
else:  
    try:   
        Path(path4).mkdir(parents=True) # parents=True ria os diretórios pais 
    except: FileExistsError
    print("Nao e possivel criar uma pasta ja existente!")



