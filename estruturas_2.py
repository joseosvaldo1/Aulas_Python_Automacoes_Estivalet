#Estruturas Condicionais_2:
age = int(input("Qual a sua idade? => "))
if age < 13:
    print("Child! Kid!")
elif (age >= 13 and age <=19):
    print("Teenager! Adolescent!")
elif (age > 19 and age <=60):
    print("Adult! Grown Up!")
else:
    print("Elderly! Aged!")