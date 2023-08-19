import pandas as pd

# Load the data from the Excel file
data = pd.read_excel('S:\projects\moderate questions\Data analyst Data.xlsx')

# Filter the data to only include students who know about the event from their colleges
college_students = data[data['Specify in "Others" (how did you come to know about this event)'] == 'College']

# Count the number of students who know about the event from their colleges
num_college_students = len(college_students)

print(f'There are {num_college_students} students who know about the event from their colleges.')

# Group the data by college and count the number of students in each college
college_counts = college_students.groupby('College Name').size()

# Sort the colleges by the number of students in descending order
top_5_colleges = college_counts.sort_values(ascending=False).head(5)

print('The top 5 colleges with the most students who know about the event are:')
print(top_5_colleges)

