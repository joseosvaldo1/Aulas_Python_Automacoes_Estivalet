"""
Arquivos PDF (Parte III):

* Combinar Arquivos PDF:

"""
import PyPDF2

def PDFmerge(pdfs, output):
    pdf_merger = PyPDF2.PdfFileMerger()
    
    for pdf in pdfs:
        pdf_merger.append(pdf)
    
    with open(output,'wb') as f:
        pdf_merger.write(f)

def main():
    pdfs = [r'.\PDF\example.pdf',r'.\PDF\rotate_example.pdf']
    output = r'.\PDF\combined_example.pdf'
    PDFmerge(pdfs,output)

main()
