""" Dicionários (continuação)"""
# Adicionando e atualizando chaves e valores de um dicionário:
print("Exemplo_1:")
car = {'brand': 'Ford', 'model': 'Mustang', 'year': '1964'}
# Adicionando um item:
print(f" car antes = {car} ")
# car['color'] = 'Red'
# Usando - se o método 'update':
car.update({'color':'Red'})      # Criando item 
car.update({'model': 'Ferrari'}) # Atualizando item
print(f" car depois = {car}")
print(" ")
print("Exemplo_2:")
# Excluindo - se itens de um dicionário:
# Para excluir itens, devemos usar o método 'del' e especificar a chave
# do item a ser excluído.
print(f" car antes = {car} ")
del car['year']
print(f" car depois = {car}")
print(" ")
print("Exemplo_3:")
# Excluindo - se itens de um dicionário:
# Caso desejarmo guardar o valor do item excluído, utilizamos o método 
# pop():
car2 = {'brand': 'Ford', 'model': 'Mustang', 'year': '1964'}
print(f"car2 antes = {car2} ")
year2 = car2.pop("year")
print(f"year2 = {year2}")
print(f"car2 depois = {car2}")
print(" ")
print("Exemplo_4:")
# Excluindo - se itens de um dicionário:
# Para excluir o último item de um dicionário, utilizamos o 
# método popitem():
car3 = {'brand': 'Ford', 'model': 'Mustang', 'year': '1964'}
print(f"car2 antes = {car3} ")
year3 = car3.popitem()
print(f"year3 = {year3}")  # Devolve uma tupla
print(f"Tipo de dado de year3 = {type(year3)}")
print(f"car3 depois = {car3}")
print(" ")
print("Exemplo_5:")
# Excluindo - se itens de um dicionário:
# Para excluir um dicionário por completo, utilizamos o método clear(0:)
car4 = {'brand': 'Ford', 'model': 'Mustang', 'year': '1964'}
print(f"car4 antes = {car4} ")
car4.clear()
print(f"car4 depois = {car4}")