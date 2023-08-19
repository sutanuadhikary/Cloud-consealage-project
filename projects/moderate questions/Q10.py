#Q10. How does the expected salary vary based on factords like 'GPA' , 'family income', 'Experience with python(Months)'?

import pandas as pd
import statsmodels.formula.api as smf

# Read the data from the Excel file
df = pd.read_excel(r'S:\projects\moderate questions\Data analyst Data.xlsx')

df = df.rename(columns={'Family Income': 'Family_Income', 'Experience with python (Months)': 'Python_Experience', 'Expected salary (Lac)': 'expected_salary'})

# extracting the numbers from the Family Income column.
def extract_numbers(s):
    return ''.join(c for c in s if c.isdigit())

df['Family_Income'] = df['Family_Income'].apply(extract_numbers).astype(float)

# Fit a linear regression model to predict expected salary based on CGPA, family income, and experience with Python
model = smf.ols('expected_salary ~ CGPA + Family_Income + Python_Experience', data=df).fit()

model.summary()
print(model.summary())

'''
