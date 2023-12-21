"""
Arquivos PDF (Parte I):

* Extrair Texto de Arquivo PDF:

"""
import PyPDF2
import sys

# Definir o encoding padrão para utf-8
sys.stdout.reconfigure(encoding='utf-8')

pdf_file = open(r'.\PDF\python_tutorial.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
# Determinando o número de páginas do arquivo PDF com o 
# método 'numPages()':
print(f"Number of Pages (python_tutorial.pdf) = {pdf_reader.numPages} pages")

# Extraindo uma página específica do arquivo PDF usando os métodos
# 'getPage()' e 'extract_text()':
page_obj = pdf_reader.getPage(1)
text_page_1 = page_obj.extract_text()


print(text_page_1)