while True:
    print("Digite sair para terminar a execuçao do programa: ")
    resposta = input()
    if resposta == 'sair':
        break
    print("Voce digitou " + resposta + " e nao ´sair'")

print("Fim!")

# O comando 'break' apenas encerra o laço de reptição quando
# uma dada condição é confirmada verdadeira. Dessa forma, o 
# o restante do código continuará ao contrário do que ocorre
# com a função sys.exit() que encera de uma vez a execução.