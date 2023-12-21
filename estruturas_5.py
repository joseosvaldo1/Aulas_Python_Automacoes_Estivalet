# Comando 'continue': É usado em laços de repetição - quando a execução
# de um programa encontra um 'continue', ele pula imediatamente para o 
# início do laço e reavalia a condição.
while True:
    print("Digite seu nome: ") 
    name = input()
    if name != "Luiz":
        continue
    print("Ola, Luiz! Digite sua senha: ")
    password = input()
    if password == "123":
        break
print("Obrigado!")