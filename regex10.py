"""
Expressões Regulares (REGEX)
- Classes de Caracteres:

* Códigos abreviados para classes comuns de caracteres 

\d => Qualquer dígito de 0 a 9; (\d = (0|1|2|3|4|5|6|7|8|9))
\D => Qualquer caractere que não seja um dígito de 0 a 9;
\w => Qualquer letra, dígito ou o caractere underscore (_). 
(Pense nisso como uma correspondência decaracteres de 
“palavra”.);
\W => Qualquer caractere que não seja uma letra, um dígito 
ou o caractere underscore (_).
\s => Qualquer espaço, tabulação ou caractere de quebra de linha. 
(Pense nisso como uma correspondência de caracteres de “espaço”.)
\S => Qualquer caractere que não seja um espaço, uma tabulação ou 
uma quebra de linha.

"""
import re
print("Exemplo_1:")
frutas = re.compile('\d+\s+\w+')
mo1 = frutas.findall('10 macas, 7 peras, 1 banana, 1 melancia')
print(f'mo1 = {mo1}')
# A expressão regular \d+\s\w+ corresponderá a textos que tenham um ou
# mais dígitos (\d+) seguidos de um caractere de espaço em branco (\s) 
# seguido de um ou mais caracteres que sejam letra/dígito/underscore 
# (\w+). O método findall() retorna todas as strings que correspondam 
# ao padrão da regex em uma lista.
print(" ")
print("Exemplo_2:")
equipamentos = re.compile('\d+\s+\w+')
mo2 = equipamentos.findall('Temos 3 computadores, 25 mouses a venda')
print(f'mo2 = {mo2}')