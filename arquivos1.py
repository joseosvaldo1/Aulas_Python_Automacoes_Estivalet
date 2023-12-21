"""
Arquivos - Parte I:

* Introdução:

- Um arquivo tem duas propriedades fundamentais: um nome de 
arquivo e um path.
- O path especifica a localização de um arquivo no computador. 
Por exemplo, há um arquivo em meu laptop com Windows 7 cujo 
nome é projects.docx no path C:\Users\asweigart\Documents.
- A parte do nome do arquivo após o último ponto é chamada de 
extensão do arquivo e informa o seu tipo. project.docx é um 
documento Word, e Users, asweigart e Documents referem-se a 
pastas (também chamadas de diretórios).
- A parte referente a C:\ do path é a pasta-raiz, que contém todas 
as demais pastas. No Windows, a pasta-raiz chama-se C:\ e é também 
chamada de drive C:. No OS X e no Linux, a pasta-raiz é /.
- No Windows, os paths são escritos com barras invertidas (\) como 
separador entre os nomes das pastas. No OS X e no Linux, porém, 
utilize a barra para frente (/) como separador de path. Se quiser 
que seus programas funcionem em todos os sistemas operacionais, 
seus scripts Python deverão ser escritos para tratar ambos os casos.
- Felizmente, isso é simples de fazer com a função os.path.join(). 
Se você lhe passar os valores de string com os nomes individuais dos 
arquivos e das pastas de seu path, os.path.join() retornará uma string 
com um path de arquivo que utilizará os separadores corretos de path. 
Digite o seguinte no shell interativo:
# >>> import os
# >>> os.path.join('usr', 'bin', 'spam')
'usr\\bin\\spam'

"""

