"""
Expressões Regulares (REGEX)

- Uma ou mais ocorrências:

    Enquanto * quer dizer “corresponda a zero ou mais”, o + (ou sinal de adição)
quer dizer “corresponda a um ou mais”. De modo diferente do asterisco, que
não exige que seu grupo esteja presente na string correspondente, o grupo que
antecede um sinal de adição deve aparecer pelo menos uma vez. Ele não é
opcional

"""
import re
print("Exemplo_1:")

uma_ou_mais_ocorrencia = re.compile('Pytho+n')
mo1 = uma_ou_mais_ocorrencia.search('Curso de Python')
mo2 = uma_ou_mais_ocorrencia.search('Curso de Pythoooooooon')
mo3 = uma_ou_mais_ocorrencia.search('Curso de Pythn')
print(f"mo1 = {mo1.group()}")
print(f"mo2 = {mo2.group()}")
#print(f"mo3 = {mo3.group()}")
print(" ")