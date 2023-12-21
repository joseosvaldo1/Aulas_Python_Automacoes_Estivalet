# Funções em Python:
"""
Objetivo: Agrupar blocos de códigos que serão 
executados múltiplas vezes.
vantagens do Uso de Funções:
1) Código organizado;
2) Facilita a manutenção e a leitura do código;
3) Possibilita o usod de parãmetros.
"""
print("Exemplo_1:")
def Hello():
    print("Hello, World!!!")

print("Antes de chamar a funcao Hello:")
Hello()
print("Depois de chamar a funcao Hello")

print(" ")
print("Exemplo_2:")
def Hello(name):
    print("Hello, " + name +"!!!")

print("Antes de chamar a funcao Hello:")
Hello("Jose")
print("Depois de chamar a funcao Hello")