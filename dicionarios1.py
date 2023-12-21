"""
# Dicionários: 
- São coleções mutáveis de itens cujos elementos
são armazenados de forma ordenada( a partir da
versão do 3.7 do Python).
- Os elementos de um dicionário em Python contêm
uma chave(key) e um valor(value);
- A chave serve para indexar um elemento;
- Um dado valor corresponde a uma unica chave.
- Sintaxe: dict = {"chave": "valor"}

"""
print("Exemplo_1: ")
# Dicionário de alunos:
# alunos = {'nome1': 'Joao'}
alunos = dict(nome = 'Joao')
print(" ")
print("Exemplo_2: ")
car = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
print(f"car = {car}")
print(f"car[model] = {car['model']}")
print(f"car[model] = {car.get('model')}")
print(f"car[color] = {car.get('color', 'key no found')}")
print(" ")
print("Exemplo_3:")
# Obtendo as chaves pelo método 'key()':
for key in car.keys():
    print(f"key = {key}: value = {car[key]}") 

print(" ")
print("Exemplo_4:")
notas = {'Math': 8.3, 'Portuguese': 6.4, 'History': 7.1, 'English': 9.0}
# Obtendo os valores pelo método 'value()':
for notas in notas.values():
    print(f"Notas = {notas} ")
print(" ")
print("Exemplo_5: ")
for key, value in car.items():
    print(f"car[{key}] = {value}")
print(" ")
# Verificando a existência de chaves e valores:
car2 = {'color': 'Red', 'brand': 'Ford', 'model': 'Ferrari', 'year': '1964'}
if 'color' in car2:
    print(f"Color is: {car2['color']}")
else:
    print('Color is not informed.')

print(" ")
print("Exemplo_6: ")
if 'Mustang' in car2.values():
    print(f"OK")
else:
    print('There is not model of car.')