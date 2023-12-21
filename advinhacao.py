import random
secret_number = random.randint(1,20)
print("Estou pensando num numero de 1 a 20!")
print("Tente advinhar qual número!")
print("Você tem sete tentativas!")

for tentativas in range(1,8):
    print("Tente advinhar o numero: ")
    guess = int(input())
    if guess < secret_number:
        print("Sua tentativa foi muito baixa!")
    elif guess > secret_number:
        print("Sua tentativa foi muito alta!")
    else:
        break

if guess == secret_number:
    print("Parabens, você acertou o numero em " + str(tentativas) + 
          " tentativas!" )
else:
    print("Que pena! Voce nao conseguiu acertar o numero!")
 