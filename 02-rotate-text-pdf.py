"""
Arquivos PDF (Parte II):

* Rotacionar Arquivos PDF:

"""
import PyPDF2

def PDFRotate(origin_file_name, new_file_name, rotation):
    pdf_file = open(origin_file_name, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    pdf_writer = PyPDF2.PdfFileWriter()
    
    for page in range(pdf_reader.numPages):
        page_obj = pdf_reader.getPage(page)
        page_obj.rotate_clockwise(rotation)
        pdf_writer.add_page(page_obj)
    
    new_file = open(new_file_name,'wb')
    pdf_writer.write(new_file)
    pdf_file.close()
    new_file.close()

def main():
    origin_file_name = r'.\PDF\example.pdf'
    new_file_name = r'.\PDF\rotate_example.pdf'
    rotation = 90
    PDFRotate(origin_file_name,new_file_name,rotation)

main()

