# Tratamento de Exceções em Python - Múltiplas Exceções:


def divisao(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Error: Invalid Argument!")
    except TypeError:
        print("Error: Invalid Type!")
    finally:
        print("Finalizando!") 


print(divisao(33,2))
print(divisao(12,'a'))
print(divisao(5,0))
print(divisao(1,3))