"""

Arquivos PDF (Parte V) - Parte II:

* Adicionar Marca D´água a um PDF:

proteger arquivos PDF com senhas:

"""
import PyPDF2
import sys

# Definir o encoding padrão para utf-8
sys.stdout.reconfigure(encoding='utf-8')

f = open(r'.\PDF\com_senha.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)
print(f"O arquivo 'com senha' esta criptogrado com senha: {pdf_reader.is_encrypted}")

pdf_reader.decrypt(b'senha')
page = pdf_reader.getPage(12)
print(page.extractText())

f.close()