"""
Compreensão de Listas:

- Código mais curto e eficaz;
- Código executado mais rápido (cerca de 35% mais rápido que o 'for');
- Utiliza a noção de conjuntos matemáticos;

- Usando o 'for':
for(conjunto de valores a iterar):
    if(filtro condicional):
        expressão de retorno
        
- Usando a 'list comprehencion':
lista = [elemento1, elemento2, ...]
nova_lista = [expressão de retorno() for (conjunto de valores a iterar) 
            if(filtro condicional)]

"""

print("Exemplo_1: ")

fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']

new_list = [x for x in fruits if x != 'apple']
print(f"new_list = {new_list}")
print(" ")
print("Exemplo_2")
new_list2 = [x for x in range(10) if x < 5]
print(f"new_list2 = {new_list2}")
print(" ")
print("Exemplo_3: ")

new_list3 = [x.upper() for x in fruits] 
print(f"new_list3 = {new_list3}")
print(" ")
print("Exemplo_4: ")

new_list4 = [x if x != 'banana' else 'orange' for x in fruits] 
print(f"new_list4 = {new_list4}")
print(" ")
print("Exemplo_5")
# x pertece ao |N tal que x <= 100 e x é uma raiz quadrada:
roots = []

for i in range(1, 101):           # Iterador
    if int(i**0.5) == i**0.5:     # Filtro Condicional
        roots.append(i)           # Expressão de retorno

print(f"roots = {roots} ")

roots2 = [i for i in range(1,101) if int(i**0.5) == i**0.5]
print(f"roots2 = {roots2}")

