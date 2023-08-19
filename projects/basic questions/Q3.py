import pandas as pd

# Read the data from the Excel file
data = pd.read_excel(r'S:\projects\basic questions\Data analyst Data.xlsx', usecols='J')

# Count the value through the data from the excel file.
x = data['Year of Graduation'].value_counts()

# print the value
print(x)
