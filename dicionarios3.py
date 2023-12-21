""""
Dicionários (continuação):

"""
# Copiando um dicionário:
# Devemos utilizar o método 'copy()':
print("Exemplo_1:")
car = {'brand': 'Ford', 'model': 'Ferrari', 'year': '1964'}
car2 = car.copy()
print(f"car = {car}")
print(f"car2 = {car2}")
print(" ")
print(f"car2 ANTES = {car2}")
car2['color'] = 'Red'
print(f"car2 DEPOIS = {car2}")
print(" ")
print("Exemplo_2: ")
#Definindo valores padrões - default:
"""
# Usando um teste condicional: 
if 'color' not in car:
    car['color'] = 'Red'

print(f'car = {car}')
"""
# Usando o método set default:
car.setdefault('color', 'Red')
print(f'car = {car}')
"""
Observação: o Método 'setdefault()' só irá funcionar
se a chave do item não existir no dicionário. 
"""
print(" ")
print("Exemplo_3")
message = "Eu estou apredendo Python com o professor Luiz"
count = {}
for char in message:
    count.setdefault(char,0)
    count[char] +=1

print(f"count = {count}")

print(" ")
print("Exemplo_4:")
car = {'brand': 'Ford', 'model': 'Ferrari', 'year': '1964'}
extra_info = {'owner': 'Luiz', 'price': '200k'}
car_plus_extra = {**car,**extra_info}
print(f"car_plus_extra = {car_plus_extra}")