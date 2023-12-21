"""
Planilhas Excel (Parte V): 

*Inserindo e Excluindo Colunas das Planilhas:


"""
import openpyxl
print("Exemplo_1:")
wb = openpyxl.load_workbook(r'.\planilhas\sales.xlsx')
sheet = wb.active
sheet.delete_cols(1)
wb.save(r'.\planilhas\sales_mod.xlsx')
print(" ")
print("Exemplo_2:")
sheet = wb.active
sheet.insert_cols(2)
wb.save(r'.\planilhas\sales_mod2.xlsx')