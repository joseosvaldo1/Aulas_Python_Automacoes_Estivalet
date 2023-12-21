"""
For em Listas:

"""
#Lista 'dogs':
dogs = ['Spike', 'Duke', 'Rex', 'Skipper']

print("Exemplo 1: ")
# Usando 'for' com a variável de controle 'i':
print("Usando o metodo 'range': ")
for i in range (len(dogs)):
    print("Index " + str(i) + ' in dog list is: ' + dogs[i])

print(" ")
print("Exemplo_2:")
print(" Usando o metodo 'enumerate':")
# Usando o método 'enumerate':
for index, dog in enumerate(dogs):
    print("Index " + str(index) + ' in dog list is: ' + dog)

