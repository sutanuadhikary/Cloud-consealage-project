import pandas as pd

# Read the data from the Excel file
data = pd.read_excel(r'S:\projects\basic questions\Data analyst Data.xlsx', usecols='M')

# Count the value through the data from the excel file.
x = data['Experience with python (Months)'].value_counts()

# Print the value
print(x)
