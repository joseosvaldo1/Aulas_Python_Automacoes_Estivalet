"""

Arquivos PDF (Parte V):

* Adicionar Marca D´água a um PDF:

proteger arquivos PDF com senhas:

"""
import PyPDF2
f = open(r'.\PDF\example.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)
pdf_writer = PyPDF2.PdfFileWriter()

for page in range(pdf_reader.numPages):
    pdf_writer.add_page(pdf_reader.getPage(page))


pdf_writer.encrypt('senha')
result_pdf = open(r'.\PDF\com_senha.pdf','wb')
pdf_writer.write(result_pdf)