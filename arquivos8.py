"""
Trabalhando com Arquivos (Parte VIII):

* Escrevendo Arquivos de Texto:

- Em Python, há três passos para ler e escrever em arquivos:
1. Chamar a função open() para que um objeto File seja retornado.
2. Chamar o método read() ou write() no objeto File.
3. Fechar o arquivo chamando o método close() no objeto File 

# Abrindo arquivos com a função open():
- Para abrir um arquivo com a função open(), passe um path em forma 
de string indicando o arquivo que você deseja abrir; poderá ser um 
path absoluto ou relativo. A função open() retorna um objeto File.


"""
import os

print("Exemplo_1:")
# Usando o método 'write()':
lines_1 = ['Readme', 'How To Write Text Files in Python']
path_1 = r'C:\Users\Usuário\Desktop\Osvaldo\Work Spaces\ws-python_estivalet\arquivos'
file_name_1 = r'Readme.txt'
path_2 = os.path.join(path_1, file_name_1)
with open(path_2,'w') as f1:
    for line in lines_1:
        f1.write(line)
        f1.write('\n')

f1.close()

print(" ")


print("Exemplo_2:")
lines_2 = ['line 1 ', 'texto xyz ', 'Python e legal']
path_3 = r'C:\Users\Usuário\Desktop\Osvaldo\Work Spaces\ws-python_estivalet\arquivos'
file_name_2 = r'arquivo.txt'
path_4 = os.path.join(path_3, file_name_2) 
with open(path_4,'w') as f2:  # Escreve as estring de lines_2 na mesma linha
    f2.writelines(lines_2)

f2.close()

print(" ")
print("Exemplo_3:")
lines_3 = ['line 1 ', 'texto xyz ', 'Python e legal']
path_4 = r'C:\Users\Usuário\Desktop\Osvaldo\Work Spaces\ws-python_estivalet\arquivos'
file_name_2 = r'arquivo2.txt'
path_5 = os.path.join(path_4, file_name_2) 
with open(path_5,'w') as f3:  # Escreve as estring de lines_2 na mesma linha
    f3.write('\n'.join(lines_2))
print (" ")
print("Exemplo_4:")
# Para adicionar novas linhas em uma arquivo já existente, usaremos o 
# método append():
with open(path_5, 'a') as f4:
    f4.write("\n 'MAIS UMA LINHA \n MAIS OUTRA LINHA")

f4.close()

print(" ")