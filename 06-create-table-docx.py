"""
Documentos Word (Parte IV):


* Criando Tabelas no Word:

"""
import docx
doc = docx.Document()
list_of_tuples = [("Betty", 45), ("John", 84), ("Malik", "34"), ("Jose", 20)]
table = doc.add_table(1,2)
heading_cells = table.rows[0].cells
heading_cells[0].text = "Name"
heading_cells[1].text = "Age"
for index, tuple in enumerate(list_of_tuples):
    cells = table.add_row().cells
    cells[0].text = tuple[0]
    cells[1].text = str(tuple[1])

path_tables_docx = r'.\word\tables.docx'
doc.save(path_tables_docx)