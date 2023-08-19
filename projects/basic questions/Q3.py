# Q3. What is the distribution of students across different graduation years?
import pandas as pd

# Read the data from the Excel file
data = pd.read_excel(r'S:\projects\basic questions\Data analyst Data.xlsx', usecols='J')

# Count the value through the data from the excel file.
x = data['Year of Graduation'].value_counts()

# print the value
print(x)

'''conslusion: Year of Graduation
2023    1536
2024    1511
2025    1292
2026     555 '''
