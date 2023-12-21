"""
Arquivos PDF (Parte IV):

* Adicionar Marca D´água a um PDF:


"""
import PyPDF2

def add_watermarker(water_file, page_obj):
    with open(water_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        page_obj.mergePage(pdf_reader.getPage(0))
    
    return page_obj

def main():
    watermark = r'./PDF/watermark.pdf'
    orig_file = r'./PDF/example.pdf'
    new_file = r'./PDF/watermark_example.pdf'

    with open(orig_file, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        pdf_writer = PyPDF2.PdfFileWriter()
        
        for page in range(pdf_reader.numPages):
            page_watermark = add_watermarker(watermark, pdf_reader.getPage(page))
            pdf_writer.addPage(page_watermark)

        with open(new_file, 'wb') as f:
            pdf_writer.write(f)

main()