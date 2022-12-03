import pandas as pd


df_excel = pd.read_excel(io = "../polipecas_stock_220919.xlsx")
df_csv = pd.read_csv("combined.csv")


print(df_excel.iloc[68])