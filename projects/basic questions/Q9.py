import pandas as pd
from scipy import stats

# Load the data from the Excel file
df = pd.read_excel(r'S:\projects\basic questions\Data analyst Data.xlsx')

def extract_numbers(s):
    return ''.join(c for c in s if c.isdigit())

# Apply the function to the column
df['Family Income'] = df['Family Income'].apply(extract_numbers)

# Convert the column to a numeric data type
df['Family Income'] = pd.to_numeric(df['Family Income'])
# Clean the data
df = df[(df['CGPA'] >= 0) & (df['CGPA'] <= 10)]
# Calculate the correlation
corr, p_value = stats.pearsonr(df['Family Income'], df['CGPA'])
print(f'Correlation: {corr:.2f}')
print(f'P-value: {p_value:.2f}')