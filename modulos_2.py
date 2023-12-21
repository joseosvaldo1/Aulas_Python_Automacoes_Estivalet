#Módulo sys:
import sys
while True:
    print("Digite sair para terminar a execuçao do programa: ")
    resposta = input()
    if resposta == 'sair':
        sys.exit()
    print("Voce digitou " + resposta + " e nao ´sair'")

# A função sys.exit() termina a execução do programa como um todo.