"""
Trabalhando Com Arquivos (Parte II)

* Validação de Caminhos:

- Muitas funções Python falharão gerando um erro se você lhes fornecer um
path inexistente. O módulo os.path disponibiliza funções para verificar 
se um dado path existe e se é um arquivo ou uma pasta.
• Chamar os.path.exists(path) retornará True se o arquivo ou a pasta
referenciada no argumento existir e retornará False caso contrário.
• Chamar os.path.isfile(path) retornará True se o argumento referente ao 
path existir e for um arquivo e retornará False caso contrário.
• Chamar os.path.isdir(path) retornará True se o argumento referente ao 
path existir e for uma pasta e retornará False caso contrário.

"""
import os
from pathlib import Path

print("Exemplo_1:")
win_dir = Path(r'C:\Windows')
non_exist_dir = Path(r'C:\xyz') 
calc_file = Path(r'C:\windows\system32\calc.exe')
print(f"win_dir_exists = {win_dir.exists()} ")
print(f"win_dir_is_dir = {win_dir.is_dir()} ")
print(30*'-')
print(f"non_exist_dir_exists = {non_exist_dir.exists()} ")
print(f"non_exist_dir_is_dir = {non_exist_dir.is_dir()} ")
print(f"non_exist_dir_is_file = {non_exist_dir.is_file()} ")
print(30*'-')
print(f"calc_file_is_file = {calc_file.is_file()} ")
print(f"calc_file_is_dir = {calc_file.is_dir()} ")