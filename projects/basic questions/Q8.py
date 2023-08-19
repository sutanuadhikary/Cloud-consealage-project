# Q8. What is the average GPA for student from each city?

import pandas as pd

# Load the data from the Excel file
data = pd.read_excel(r'S:\projects\basic questions\Data analyst Data.xlsx')

# Calculate the average CCGPA for each city
average_CGPA = data.groupby('City')['CGPA'].mean()

# Print the result
print('Average CCGPA for each city:', average_CGPA)

'''
Average CCGPA for each city: City
Agartala     7.660714
Agra         8.046429
Ahemdabad    8.190385
Ajmer        8.284314
Akola        8.021429
               ...
Vidisha      7.738095
Vijaywada    7.986364
Wardha       8.328571
konark       8.071429
kullu        7.878571
'''
