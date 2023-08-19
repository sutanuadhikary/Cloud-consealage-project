import pandas as pd

# Load the Excel file
df = pd.read_excel(r'S:\projects\basic questions\Data analyst Data.xlsx',usecols="A,N", engine='openpyxl')

# Get the details of a specific student by name
student_name = input('Enter the name of the student: ')
student_details = df.loc[df['First Name'] == student_name]

# Display the student details
print(student_details)