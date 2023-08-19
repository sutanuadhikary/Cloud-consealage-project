#Q14. How many students are gratuating by the end of 2024?

import pandas as pd

# Load the data from the Excel file
data = pd.read_excel(r'S:\projects\moderate questions\Data analyst Data.xlsx')

# Filter the data to only include students graduating by the end of 2024
graduating_students = data[data['Year of Graduation'] <= 2024]

# Count the number of graduating students
num_graduating_students = len(graduating_students)

print(f'There are {num_graduating_students} students graduating by the end of 2024.')

'''
There are 3047 students graduating by the end of 2024.
'''
