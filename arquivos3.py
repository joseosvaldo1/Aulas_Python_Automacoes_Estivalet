"""
Trabalhando com Arquivos-Parte III
* Caminhos Absolutos e Caminhos Relativos:

- Há duas maneiras de especificar um path de arquivo.
#  Um path absoluto, que sempre começa com a pasta-raiz.
#  Um path relativo, que é relativo ao diretório de trabalho 
atual do programa.

-Temos também as pastas ponto (.) e ponto-ponto (..). Essas não são 
pastas de verdade, mas nomes especiais que podem ser usados em um path.
Um único ponto para um nome de pasta é a forma abreviada de “este 
diretório”.Dois pontos (ponto-ponto) quer dizer “a pasta pai”.
- O .\ no início de um path relativo é opcional. Por exemplo, 
.\spam.txt e spam.txt referem-se ao mesmo arquivo.

# módulo pathlib:
- is_absolute(): Retorna verdadeiro se o caminho de um arquivo for 
absoluto;

# módulo os.path:
- os.pathabspath(path): retornará uma string com o path absoluto
referente ao argumento. Essa é uma maneira fácil de converter um 
path relativo em um path absoluto.

- os.path.isabs(path): retornará 'True' (verdadeiro) se o argumento 
for um path absoluto e 'False' (falso) se for um path relativo.

- os.path.relpath(path, início/start): retornará uma string contendo 
um path relativo ao path início/start para path. Se início não for 
especificado, o diretório de trabalho atual será usado como path de 
início.


"""
from pathlib import Path
import os
print("Exemplo_1:")
pwd = Path.cwd()
print(f'pwd = {pwd}')
pwd_is_absolute = pwd.is_absolute()
print(f'pwd_is_absolute = {pwd_is_absolute}')
path1 = Path('temp','python')
print(25*'=')
path1_is_absolute = path1.is_absolute()
print(f'path1 = {path1}')
print(f'path1_is_absolute = {path1_is_absolute}')
# Transformando caminhos relativos em absolutos:
print(" ")
print(25*'-')
path_rel = Path('Desktop', 'Osvaldo', 'Work Spaces','ws-python_estivalet')
pwd = Path.cwd()
path_abs = path_rel / pwd # => primeiro o relativo / working directory
# No terminal do Python, deve-se colocar o contrário.
print(f"path_abs = {path_abs}")
print(" ")
print(25*'-')
print("Exemplo_2:")
abs_path1 = os.path.abspath('.')
print(f'abs_path1 = {abs_path1}')
abs_path2 = os.path.abspath('.\\Documents')
print(f'abs_path2 = {abs_path2}')
is_abs1=os.path.isabs('.')
print(f'is_abs1 = {is_abs1}')
print(" ")
print(25*'-')
print("Exemplo_3:")
path_rel1 = os.path.relpath('c:\\windows','c:\\') 
print(f"path_rel1 = {path_rel1}")
print(25*'=')
path_rel2 = os.path.relpath('c:\\windows','C:\\Users\\Usuário\\Desktop\\Osvaldo')
print(f"path_rel2 = {path_rel2}")
print(25*'=')
path_rel3 = os.path.relpath('C:\\Users\\Usuário\\Desktop\\Osvaldo','C:\\Users\\Usuário')
print(f"path_rel3 = {path_rel3}")