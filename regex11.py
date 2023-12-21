"""
Expressões Regulares:
* Criando nossas próprias classes de caracteres:

- Haverá ocasiões em que você vai querer fazer a correspondência de um
conjunto de caracteres, porém as classes abreviadas de caracteres 
(\d, \w, \s eassim por diante) serão amplas demais. Você pode definir 
sua própria classe de caracteres usando colchetes. Por exemplo, a classe 
de caracteres [aeiouAEIOU] corresponderá a qualquer vogal, tanto 
minúscula quanto maiúscula. 

- Também é possível incluir intervalos de letras ou de números usando um
hífen. Por exemplo, a classe de caracteres [a-zA-Z0-9] corresponderá a 
todas as letras minúsculas, às letras maiúsculas e aos números.

- Observe que, nos colchetes, os símbolos normais de expressão regular 
não são interpretados. Isso quer dizer que não é necessário escapar os 
caracteres ..,*, ? ou () com uma barra invertida na frente. Por exemplo, 
a classe de caracteres [0-5.] corresponderá aos dígitos de 0 a 5 e um 
ponto. Não é preciso escrever essa classe como [0-5\.].

- Ao inserir um acento circunflexo (^) logo depois do colchete de abertura 
daclasse de caracteres, podemos criar uma classe negativa de caracteres. 
Umaclasse negativa de caracteres corresponderá a todos os caracteres que 
não estejam na classe de caracteres.


"""
import re
print("Exemplo_1: ")
vogais = re.compile('[aeiouAEIOU]')
mo1 = vogais.findall('Cuso de Python do Zero a Automacao')
print(f"mo1 = {mo1}")
print(" ")
print("Exemplo_2: ")
alfanumerico = re.compile('[a-zA-Z0-9]')
mo2 = alfanumerico.findall('Cuso de Python do Zero a Automacao')
print(f"mo2 = {mo2}")
print(" ")
print("Exemplo_3: ")
nao_vogais = re.compile('[^aeiouAEIOU]')
mo3 = nao_vogais.findall('Cuso de Python do Zero a Automacao')
print(f"mo3 = {mo3}")
print(" ")