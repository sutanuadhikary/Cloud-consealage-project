import pandas as pd

# Load the data from the Excel file
data = pd.read_excel('S:\projects\moderate questions\Data analyst Data.xlsx')

# Filter the data to only include students who attend events related to data science
data_science_students = data[data['Events'].str.contains('data science', case=False)]

# Count the number of students who attend events related to data science
num_data_science_students = len(data_science_students)

print(f'There are {num_data_science_students} students who attend events related to data science.')
