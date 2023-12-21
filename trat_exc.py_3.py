# Tratamento de Exceções em Python - Lançando Execeções:


def test(x):
    if not type(x) is int:
        raise Exception("Only integers allowed!")
    if x < 0:
        raise Exception("Sorry, no numbers bellow zero!")
    else:
        print("A raiz quadrada de x eh: ")
        print(x**0.5)

test(4)
test(-4)
test(1.25)