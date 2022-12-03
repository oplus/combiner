import pandas as pd
import tkinter as tk
import tkinter.filedialog as fd
from utilities import *
import os






#for file in os.listdir(): print(file)


#columns_order: manufacturer/partnumber/quantity/price
#first number in the list refer to where data starts (how many rows before)
#other four numbers refer to manufacturer/partnumber/quantity/price in order
file_columns = {
	"metal":	{	"header": 0, 
					"columns": ["Fabricante", "Codigo_fornecedor", "quantity", "PRECO_LIQUIDO"],
					"special_operation": None
				},

	"medauto":	{	"header": 0, 
					"columns": ["Fornecedor", "NUMERO DA PEÇA", "ESTOQUE", "PREÇO"],
					"special_operation": None
				},
	"lucios": 	{	"header": 0, 
					"columns": ["Fabricante", "Código Lucios", "Disponibilidade", "Preço"],
					"special_operation": None
				},
	"carbwel": 	{	"header": 0, 
					"columns": ["Fabricante", "Código Fabricante", "Disponivel", "PrcVenda"],
					"special_operation": None
				},
	"mte": 	{	"header": 0, 
					"columns": ["COD MTE", "QTD. ESTOQUE", "PREÇO"],
					"special_operation": mte_process
				},
	"sueyasu": 	{	"header": 0, 
					"columns": ["NOME DO FABRICANTE", "CODIGO DA PEÇA (FABRICANTE)", "QUANTIDADE EM ESTOQUE", "PREÇO"],
					"special_operation": sueyasu_process
				},
	"polipecas":{	"header": 15, 
					"columns": ["COD. FORNECEDOR", "PREÇO"],
					"special_operation": polipecas_process
				},
}






def read_file(file, supplier_code, header, special_operation):
	if "xlsx" in file or "xls" in file.lower():
		df = pd.read_excel(
			io=Fr"{file}", 
			header = file_columns[supplier_code]["header"], 
			usecols= file_columns[supplier_code]["columns"]
			)[file_columns[supplier_code]["columns"]] #To maintain parsed columns orders

		if file_columns[supplier_code]["special_operation"]:
			df = file_columns[supplier_code]["special_operation"](df)

		df.columns = ["Manufacturer", "Partnumber", "Quantity", "Price"]
		
		df["supplier"] = supplier_code

	elif "txt" in file:
		pass

	elif "csv" in file:
			df = pd.read_csv(file, 
			header = None, 
			usecols=file_columns[supplier_code][1:], 
			skiprows = file_columns[supplier_code][0],
			sep=";", 
			encoding= "ISO-8859-1")[file_columns[supplier_code][1:]]
	else:
		print("unkown file formate: ", file)

	return df







if __name__ == "__main__":
	root = tk.Tk()
	filez = fd.askopenfilenames(parent=root, title='Choose a file')
	all_df = []

	for file in filez:
		file_columns_keys = list(file_columns.keys())
		for supplier_code in file_columns_keys:
			if supplier_code in file.lower():
				print(file, "====", supplier_code, file_columns[supplier_code]["header"])
				all_df.append(read_file(
					file, 
					supplier_code, 
					header = file_columns[supplier_code]["header"], 
					special_operation = file_columns[supplier_code]["special_operation"]))
	pd.concat(all_df, ignore_index = True).to_csv('combined.csv')

