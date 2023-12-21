"""
# Tuplas:
- As tuplas são utilizadas para armazenar múltiplos itens
em uma única variável.
- Características das Tuplas:
1. Elas são ordenadas - os itens tem ordens definidas e 
essas ordens não podem ser modificadas;
2. Ela é imutável - Não é possível modificar, adicionar ou
remover itens depois que a tupla é criada.
3. Elas permitem itens duplicados - como ela é indexida, eles
podem ter itens com um mesmo valor.

- A forma de acessar os itens de uma tupla é o mesmo utilizado 
pelas listas.
- Para verificar se um item pertence ou não a uma tupla, 
podemos usar os operador 'in' e 'not in'. 

"""
print("Exemplo_1: ")
t1 = ('apple', 'banana','cherry','apple','cherry')

print(f"Tipo de Dado de t1 = {type(t1)}")
print(f"Tupla t1 = {t1}")
print(f"Tamanho da Tupla t1 = {len(t1)}")
print(" ")

print("Exemplo_2: ")
t2 = ('apple',)
print(f"Tipo de Dado de t2 = {type(t2)}")
print(f"Tupla t2 = {t2}")
print(f"Tamanho da Tupla t2 = {len(t2)}")
print(" ")

print("Exemplo_3: ")
tupla1 = ('apple', 'banana', 'cherry')
tupla2 = (1, 5, 7, 9, 3)
tupla3 = (True, False, False)
tupla4 = ('abc', 34, True, 40, 'male')