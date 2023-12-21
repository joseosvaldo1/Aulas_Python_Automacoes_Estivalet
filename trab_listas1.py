"""
Trabalhando Com Listas:

"""
dog_names = []

while True:
    print("Enter the name of the dog: " + str(len(dog_names)+1) +
        ' (OR enter nothing to stop.): ')
    name = input()
    if name == '':
        break
    
    dog_names = dog_names + [name]

print("The dog names are: " + str(dog_names))

for name in dog_names:
    print(' ' + name) 