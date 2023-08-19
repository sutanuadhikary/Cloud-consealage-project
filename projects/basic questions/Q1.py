# Q1.How many unique students are included in the dataset?

import pandas as pd

# Read the data from the Excel file
df = pd.read_excel(r'S:\projects\basic questions\Data analyst Data.xlsx')

# Filter the unique students.
unique_students = df['First Name'].unique()

# The number of unique students
num_unique_students = len(unique_students)

print(f'There are {num_unique_students} unique students in the dataset.')

# Conclusion: There are 2324 unique students in the dataset. 
