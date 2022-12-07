import pandas as pd

def mte_process(df):
	#Insert empty row at index 0
	df.insert(	loc=0, 
				column='new col', 
				value=['' for i in range(df.shape[0])])
	
	#Remove first row as it is empty
	df.drop(	index=df.index[0], 
        		axis=0, 
        		inplace=True)
	return df


def sueyasu_process(df):
	#Remove first row (unwanted data)
	df.drop(	index=df.index[0], 
    			axis=0, 
    			inplace=True)
	return df


def polipecas_process(df): 
	###HARD CODED BOSCH 
	###WHAT IF THERE IS ZERO IN THE BEGINNING OF PART NUMBER

	#Adding manufacturer column and hard coding BOSCH in it
	df.insert(	loc=0, 
				column='new col', 
				value=['BOSCH' for i in range(df.shape[0])])

	#Adding empty quantity column
	df.insert(	loc=2, 
				column='new col2', 
				value=['' for i in range(df.shape[0])])

	#Removing row if there is no part number
	df = df[df["COD. FORNECEDOR"].notnull()] 

	return df


def ima_process(df):
	df.insert(	loc=0, 
				column='new col', 
				value=['' for i in range(df.shape[0])])

	#Adding empty quantity column
	df.insert(	loc=3, 
				column='new col2', 
				value=['' for i in range(df.shape[0])])

	return df


def compel_process(df):
	#Remove first row (unwanted data)
	df.drop(	index=df.index[:2], 
    			axis=0, 
    			inplace=True)
	return df


def jahu_process(df):

	#print(df[6].to_string())
	df.loc[df[6] == "JAHU PLACA PRETA", df[1]] =df[4]

	df = df.drop(df.columns[[4]], axis=1)
	return df







###SOMETIMES NO PART NUMBER IN METAL