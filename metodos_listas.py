""" 
Métodos das Listas:

"""

livros = ['Java', 'Delphi', 'SQL']
#índices:   0       1        2
# Médoto 'índex': Localiza a posição de um elemento em uma lista.
print("Metodo Index:")
print(f"A posicao de 'Java' eh: {livros.index('Java')}")
print(f"A posicao de 'Delphi' eh: {livros.index('Delphi')}")
print(f"A posicao de 'SQL' eh: {livros.index('SQL')}")
print(" ")
# Método 'append': Anexa um elemento na ultima posição da lista.
print("Metodo Append:")
print(f"Livros ANTES DA INCLUSAO = {livros}")
livros.append('Python')
print(f"Livros DEPOIS DA INCLUSAO = {livros}")
print(" ")
print("Metodo Insert:")
# Método 'insert': Anexa um elemento numa posição específica.
print(f"Livros ANTES DA INCLUSAO = {livros}")
livros.insert(1,'Ruby')
print(f"Livros DEPOIS DA INCLUSAO = {livros}")
print(" ")
print("Metodo Pop:")
# Método 'pop': Remove o último elemento de uma lista por padrão.
# Caso especifice uma posição 'n', ele removerá o elemento da 
# posição 'n': 
print(f"Livros ANTES DA EXCLUSAO = {livros}")
item1 = livros.pop()
item2 = livros.pop(1)
print(f"Elemento excluido - ultimo = {item1}")
print(f"Elemento excluido - indice 1 = {item2}")  
print(f"Livros DEPOIS DA EXCLUSAO = {livros}")
print(" ")
print("Metodo Remove: ")
# Método 'remove': Remove um elemento da lista com base no seu valor.
print(f"Livros ANTES DA EXCLUSAO = {livros}")
livros.remove('SQL')
print(f"Livros DEPOIS DA EXCLUSAO = {livros}")
print(" ")
# Método 'sort': Usado para ordenar a lista em ordem crescente
# ou em ordem crescente.
print("Metodo Sort:")
livros2 = ['Java', 'Delphi', 'SQL', 'Python']
print(f"Livros2 ANTES DA ORDENACAO = {livros2}")
livros2.sort()
print(f"Livros2 ANTES DA ORDENACAO = {livros2}")
print(" ")
# Método 'reverse': Usado para ordenar a lista em ordem decrescente 
# ou alfabética reversa.
print("Metodo Reverse:")
print(f"Livros2 ANTES DA ORDENACAO = {livros2}")
livros2.reverse()
print(f"Livros2 ANTES DA ORDENACAO = {livros2}")
print(" ")
# Método ´count': Utilizado para contar a quantidade de ocorrências
# de um dado elemento em uma lista.
print("Metodo Count:")
livros3 = ['Oracle', 'Java', 'SqlServer', 'Delphi', 'Python', 'Andorid', 'Oracle']
total_oracle = livros3.count('Oracle')
total_python = livros3.count('Python')
total_ruby = livros3.count('Ruby')
print(f"Quantidade de 'Oracle' = {total_oracle}")
print(f"Quantidade de 'Python' = {total_python}")
print(f"Quantidade de 'Ruby' = {total_ruby}")
