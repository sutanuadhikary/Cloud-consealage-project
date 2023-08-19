import pandas as pd

# Load the data from the Excel file
data = pd.read_excel(r'S:\projects\basic questions\Data analyst Data.xlsx')

# Calculate the average CCGPA for each city
average_CGPA = data.groupby('City')['CGPA'].mean()

# Print the result
print('Average CCGPA for each city:', average_CGPA)
