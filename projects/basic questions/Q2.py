#Q2. What is the average GPA of the students?

import pandas as pd

# Read the data from the Excel file
mean = pd.read_excel(r'S:\projects\basic questions\Data analyst Data.xlsx', usecols='L')

# Print the mean.
print (mean.mean())

# Conclusion: the average GPA of the students are:   CGPA    8.038476
