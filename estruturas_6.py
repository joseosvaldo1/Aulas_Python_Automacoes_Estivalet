#O Comando 'For':
"""
    Palavra chave 'for';
    Uma variável de controle;
    Palavra chave 'in';
    Função 'range';
    Dois ponto ':';
    Clásula do for(Bloco de Código).
    
"""
#Exemplos:
print("Exemplo 1:")
for i in range (5):
    print("Contando: " + str(i))
""" Neste exemplo, o 'for' itera de 0 a 4 (= i-1)
    com acréscimo - passo - de uma unidade para i. 
"""
print(" ")
print("Exemplo 2:")
for i in range (10,15):
    print("Contando: " + str(i))
""" Neste exemplo, o 'for' itera de 10 a 14 (= i-1)
    com acréscimo - passo - de uma unidade para i. 
"""
print(" ")
print("Exemplo 3:")
for i in range (0,20,2):
    print("Contando: " + str(i))
""" Neste exemplo, o 'for' itera de 0 a 19 (= i-1)
    com acréscimo - passo - de duas unidade para i. 
"""
print(" ")
print("Exemplo 4:")
for i in range (10,-1,-1):
    print("Contando: " + str(i))
""" Neste exemplo, o 'for' itera de 10 a 0 (= i-1)
    com decréscimo - passo - de -1 para i. 
"""