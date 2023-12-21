# Tratamento de Exceções em Python:
"""
    Para o tratamento de exceções em Python, temos os seguintes blocos:
    1. try: permite verificar se houve algum erro dentro de um bloco de 
    código;
    2. excpet: permite tratar algum erro que ocorreu;
    3. finally: permite executar um bloco de código independente dos 
    resultados dos blocs try e except.    
    
"""


def divisao(a, b):
    try:
        return a/b
    except: ZeroDivisionError
    print("Error: Invalid Argument!")
        

print(divisao(33,2))
print(divisao(12,4))
print(divisao(5,0))
print(divisao(1,3))