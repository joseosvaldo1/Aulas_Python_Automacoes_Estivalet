"""
Expressões Regulares (Regex):

Encontrando Padrões Sem Expressões Regulares:

1) Expressões regulares: permitem econtrar padrões em um texto
Exemplos:
- Números de telefone;
- Endereços de e-mail;
- Números de CPF/CNPJ.

"""
print("Exemplo_1: ")
#padrão: Número de telefone - (DD) XXXXX-XXXX
def is_phone_number(text):
    if len(text) != 15:
        return False
    if text[0] != '(':
        return False
    for i in range(1, 3):
        if not text[i].isdecimal:
            return False
    if text[4] != ' ':
        return False
    for i in range(5, 10):
        if not text[i].isdecimal:
            return False
    if text[10] != '-':
        return False
    for i in range(10, 15):
        if not text[i].isdecimal:
            return False    
    return True
phone1 = "(85) 33497-3797"
print(is_phone_number(phone1))
print(" ")
phone2 = '+55 (85) 3497-3797'
print(is_phone_number(phone2))
