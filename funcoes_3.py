#Retorno de Valores em Funções no Python:
def calcular_salario(qtd_horas, valor_hora):
    horas = float(qtd_horas)
    taxa = float(valor_hora)
    if horas <= 40:
        salario = horas*taxa
    else:
        horas_excedentes = horas - 40
        salario = 40*taxa + 1.50*taxa*horas_excedentes
    return salario

str_horas = input("Digite a quantidade de horas trabalhadas: ")
str_taxa = input("Digite o valor da hora trabalhada: ")
salario_calculado = calcular_salario(str_horas,str_taxa)
print("O Valor do salário e: " + str(salario_calculado))