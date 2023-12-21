"""
Método 'Random' em Listas:

"""
import random

dogs = ['Spike', 'Duke', 'Rex', 'Skipper']
# A função 'Choice' do Módulo 'Range' escolhe um elemento aleatório da lista.
print(f"Usando o metodo a funcao 'choice': {random.choice(dogs)}")
print(" ")
random.shuffle(dogs)
print(f"Usando o metodo a funcao 'shuffle': {dogs}")
