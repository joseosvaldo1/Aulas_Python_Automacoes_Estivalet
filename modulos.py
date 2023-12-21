# Utilizamos a palavra chave 'import' para importar módulos.
# Usando somente o import <módulo> no começo do código, devmos 
# obrigatoriamente colocar o nome do múdulo antes da função
# (módulo.função(parâmetros))

# Alternativamento, podemos usar a seginte estrutura no começo do 
# código <from modulo import *> e não precisaremos colocar o nome
# do módulo antes de chamar uma função do mesmo.  
 
# Exemplos:
print("Exemplo_1:")

from random import *
 
for i in range (5):
    print(randint(1,10))