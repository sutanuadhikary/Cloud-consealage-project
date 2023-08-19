#Q13. Is there a correlation between leadership skills and expected salary of the students?

import pandas as pd

# Load the data from the Excel file
df = pd.read_excel(r'S:\projects\moderate questions\Data analyst Data.xlsx', usecols='O,P')

df = df.rename(columns={'Expected salary (Lac)': 'expected_salary', 'Leadership- skills': 'leadership'})

# Convert the leadership column to a numeric value
df['leadership'] = df['leadership'].replace({'yes': 1, 'no': 0, 'no ':0})



data=pd.DataFrame(df)
# Calculate the correlation between leadership skills and expected salary
correlation = data.corr()

# Print the result
print(f'Correlation between leadership skills and expected salary: {correlation}')

'''
Correlation between leadership skills and expected salary:           
       expected_salary  leadership
expected_salary         1.000000    0.003963
leadership              0.003963    1.000000
'''
