"""
Métodos úteis para string - parte I:

"""
print("Exemplo_1:")
s = "Bem vindo ao curso de Python do professor Luiz!"
# Método 'upper()': Coloca todas as letras da string em maiúsculas.
s1 = s.upper()
print("s1 = " +s1)
print(" ")
# Método 'lower()': Coloca todas as letras da string em minúsculas.
print("Exemplo_2:")
s2 = s1.lower()
print("s2 = " +s2)
print(" ")

print("Exemplo_3:")
comando = ""
while comando.lower() != 'fim':
    print("Digite 'FIM' para terminar o programa.")
    comando = input()

print("Exemplo_4:")
# Método islower(): Verifica se todas as letras está em caixa alta: 
teste = "TUDO MAIUSCULO"
message1 = teste.islower() 
print(f"message1 = {message1}")
print(" ")
print("Exemplo_5:")
# Método islower(): verifica se todas as letras está em caixa baixa.
message2 = teste.isupper() 
print(f"message2 = {message2}")
print(" ")
print("Exemplo_6:")
# Método istitle(): Verifica se todas as palaras de uma estring começa com 
# maiúscula e são seguidas por minúscuslas. 
message3 = "Curso De Python".istitle()
print(f"message3 = {message3}" )
print(" ")
print("Exemplo_7:")
# Método isalpha(): Verifica se a string é não vazia e só tem letras.  
message4 = "Python".isalpha()
print(f"message4 = {message4}" )
print(" ")
print("Exemplo_8:")
# Método isalnum(): Verifica se a string é não vazia e tem letras e números.  
message5 = "Python3".isalnum()
print(f"message5 = {message5}" )
print(" ")
print("Exemplo_9:")
# Método isalspace(): Verifica se a string é não vazia e 
# só tem espaços em branco.  
message6 = "  ".isspace()
print(f"message6 = {message6}" )
print(" ")
print("Exemplo_10:")
# Método isdecimal(): Verifica se a string é não vazia e 
# só tem números
message7 = "123".isdecimal()
print(f"message7 = {message7}")
print(" ")
print("Exemplo_11:")
while True:
    print("Digite sua idade:")
    age = input()
    if age.isdecimal():
        break
    print("Por favor, entre com um numero para sua idade:") 
print(" ")
print("Exemplo_12:")
while True:
    print("Entre com uma senha - letras e numeros:")
    password = input()
    if password.isalnum():
        break
    print("A senha so pode conter letras e/ou numeros") 

print(" ")
print("Exemplo_13:")
# Método starswith(): Verifica se uma dada string começa uma outra 
# Retorna True/False (boolean).
message7 = "Hello, world!".startswith("Hello")
print(f"message 7 = {message7}")

print(" ")
print("Exemplo_13:")
# Método endswith(): Verifica se uma dada string termina uma outra.
# Retorna True/False (boolean).
message8 = "Hello, world!".endswith("world!")
print(f"message 8 = {message8}")
print(" ")

print("Exemplo_14:")
# Método 'join()': Útil quando temos uma lista de string e queremos 
# juntar seus elementos em uma única string.
string1 = ['cats', 'rats', 'bats']
string2 = ', '.join(string1)
print(f"string2 = {string2}")
apresentacao = ' '.join(['Meu', 'nome', 'eh', 'Luiz'])
print(f"apresemtação = {apresentacao}")

print(" ")

print("Exemplo_15:")
# Método 'join()': Útil quando temos uma string e queremos 
# separá-la em uma lista de strings.
string3 = "Meu nome eh Luiz"
lista3 = string3.split()
print(f"lista3 = {lista3}")
print(" ")
string4 = "Meu-nome-eh-Luiz"
lista4 = string4.split('-')
print(f"lista4 = {lista4}")
text = """Listeners of all backgrounds join author/journalist 
MarthaBarnette and linguist/lexicographer Grant Barrett on 
the show with their thoughts, questions, and stories about 
how language and words matter."""
lista5 = text.split("\n")
print(f"lista5 = {lista5}")