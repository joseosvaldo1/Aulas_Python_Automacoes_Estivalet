""" 
    O escopo de uma varíavel determina que ela só estará 
disponível dentro da região onde ela foi criada.
    Existem dois tipos de escopo: escopo local e escopo 
global.
    O escopo local também vale para os parâmetros de uma
função. As variáveis que são criadas dentro de uma função
ficarão contidas dentro do escopo da função.
    Uma variável criada no corpo principal do código em 
Python é chamada de variável global e pertence ao escopo
global do programa. Elas estarão disponíveis tanto no escopo
global quanto no escopo local.

"""

x = 300 # Variável 'x' definida no escopo global do código.
print("Exemplo_1: ")
def my_function():
    x = 200 # Variável 'x' definida no escopo local da função.
    print("x local: " + str(x))
    

my_function()
print("x global: "+str(x))
print(" ")

print("Exemplo_2: ")
def my_function():
    print("x local: " + str(x))
    

my_function()
print("x global: "+str(x))
print(" ")

print("Exemplo_2: ")
def my_function():
    global y 
    y = 200
    print("y local: " + str(y))
    

my_function()
print("y global: "+str(y))
print(" ")