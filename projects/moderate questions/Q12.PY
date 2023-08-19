#Q12. Do students in leadership positions during their college years tend to have heigher GPAs or better expected salary?

import pandas as pd

# Load the data from the Excel file
df = pd.read_excel(r'S:\projects\moderate questions\Data analyst Data.xlsx')

# Calculate the averages for students with leadership skills
leadership_df = df[df['Leadership- skills'] == "yes"]
if not leadership_df.empty:
    avg_leadership_gpa = leadership_df['CGPA'].mean()
    avg_leadership_salary = leadership_df['Expected salary (Lac)'].mean()
    print(f'Average GPA for students with leadership skills: {avg_leadership_gpa}')
    print(f'Average expected salary for students with leadership skills: {avg_leadership_salary}')
else:
    print('No data available for students with leadership skills')

# Calculate the averages for students without leadership skills
non_leadership_df = df[df['Leadership- skills'] == "no"]
if not non_leadership_df.empty:
    avg_non_leadership_gpa = non_leadership_df['CGPA'].mean()
    avg_non_leadership_salary = non_leadership_df['Expected salary (Lac)'].mean()
    print(f'Average GPA for students without leadership skills: {avg_non_leadership_gpa}')
    print(f'Average expected salary for students without leadership skills: {avg_non_leadership_salary}')
else:
    print('No data available for students without leadership skills')

'''Average GPA for students with leadership skills: 8.036787247087677
Average expected salary for students with leadership skills: 13.971796443899448
Average GPA for students without leadership skills: 8.040444274224436
Average expected salary for students without leadership skills: 13.795097663730372
'''
