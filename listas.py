# Listas e Tuplas - Acessando Elementos:
"""
#Listas:
- Sequencia de valores de itens ou elementos;
- Heterogênea: Pode ter itens de qualquer tipo;
- Cada Valor tem uma localização chamada de índice
- índices vão de 0 a n-1, onde 'n' é o tamanho - length -
da lista

"""
print("Exemplo_1")
lista1 = [] # lista vazia
print("Lista1: "+str(lista1))
print(lista1)
print("Tamanho da lista1: " + str(len(lista1)))
print(" ")

print("Exemplo_2")

#índices: -4  -3   -2   -1        Vai de -n a -1
lista2 =  [1,   2,   3,   40]
#índices:  0    1    2    3       Vai de 0 a n-1
print("Lista2: " + str(lista2)) 
print(lista2)
print("Tamanho da lista 2: "+str(len(lista2)))
print("lista2[0] = " + str(lista2[0]))
print("lista2[1] = " + str(lista2[1]))
print("lista2[2] = " + str(lista2[2]))
print("lista2[3] = " + str(lista2[3]))
print(" ")

print("Exemplo_3")
#         -6  -5     -4      -3   -2   -1
lista3 = [ 1, 'cat', 'dog',   3,   4,   5]
#índices:  0    1     2       3    4    5 
print("Lista3: " + str(lista3))
print("Tamanho da lista3: " + str(len(lista3)))
print(lista3)
print("lista3[0:2]: " + str(lista3[0:2]))  # Slice da Lista 3
print("lista3[0:3]: " + str(lista3[0:3]))
print("lista3[1:]: " + str(lista3[1:]))
print("lista3[:2]: " + str(lista3[:2]))
print("lista3[0:-1]: " + str(lista3[0:-1]))
print(" ")
print("Exemplo_4")
lista4 = ['animais', 123, lista3] 
print("Lista4: " + str(lista4))
print("Tamanho da lista4: " + str(len(lista4)))
print(lista4)
print("Lista4[2]: " + str(lista4[2]))
print("Lista4[2][0]: " + str(lista4[2][0]))
print("Lista4[2][1]: " + str(lista4[2][1]))
print("Lista4[2][2]: " + str(lista4[2][2]))
print(" ")
print("Exemplo_5:")
lista4 = [1,'cat', 'dog,', 3, 4, 5]
#índices  0   1     2      3  4  5
lista5 = ['animais', 123, lista4]
#índices    0         1     2

print(f"Lista4 ANTES da ALTERACAO = {lista4}")
lista4[3] = 345
print(f"Lista4 ANTES da ALTERACAO = {lista4}")
print(" ")
print("Exemplo_6:")
lista4 = [1,'cat', 'dog,', 3, 4, 5]
#índices  0   1     2      3  4  5
lista5 = ['animais', 123, lista4]
#índices    0         1     2

print(f"Lista4 ANTES da ALTERACAO = {lista4}")
lista5[2][1] = 'mouse'
print(f"Lista4 ANTES da ALTERACAO = {lista4}")
print (" ")
print("Exemplo_7:")
lista6 = ['jose', 'luiz', 'fernando']
lista7 = ['maria', 'beatriz', 'laura', 'sofia']
lista8 = lista6 + lista7
lista9 = lista6*2
print("Lista9 =" + str(lista9))
print (" ")
print("Exemplo_8:")
lista10 = ['cat', 'dog', 'mouse', 'bird' ]
#índices:   0      1      2        3

print(f"Lista10 ANTES DA EXCLUSAO = {lista10} ") 
del lista10[2]
print(f"Lista10 DEPIS DA EXCLUSAO = {lista10} ") 
print(" ")
print("Exemplo_9:")
# Saber se um elemento pertence a uma lista - usamos os 
# operadores 'in' e 'not in'
lista10 = ['cat', 'dog', 'mouse', 'bird' ]
#índices:   0      1      2        3
existe1 = 'dog' in lista10
existe2 = 'dog1' in lista10
existe3 = 'lion' not in lista10
print(f"dog esta na lista?: {existe1} ")
print(f"dog1 esta na lista?: {existe2} ")
print(f"lion nao esta na lista?: {existe3} ")
print(" ")
print("Exemplo_10:")
# Métodos 'min', 'max' e 'sum' das listas:
lista11 = [14.55, 67, 89.88, 10, 21.5] 
minimo = min(lista11)
maximo = max(lista11)
soma = sum(lista11)
print(f"Valor minimo da lista11 = {minimo}")
print(min(lista11))
print(f"O valor maximo da lista11 = {maximo}")
print(max(lista11))
print(f"O somatorio dos elementos da lista11 = {soma}")
print(sum(lista11))


