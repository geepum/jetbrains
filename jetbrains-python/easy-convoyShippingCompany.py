#!/opt/homebrew/opt/python@3.10/bin/python3

import pandas as pd

file_name = input('Input file name\n')
file_name1 = file_name.split('.')[0]

df_excel = pd.read_excel(f'./exercises/{file_name}', sheet_name='Vehicles', dtype=str, index_col='vehicle_id')

excel_shape = df_excel.shape
# print(file_name1)
df_excel.to_csv(f'./exercises/{file_name1}.csv')

print(f'{excel_shape[0]} lines were added to {file_name1}.csv')
