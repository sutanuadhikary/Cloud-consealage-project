import pandas as pd

# Load the data from the Excel file
df = pd.read_excel('S:\projects\moderate questions\Data analyst Data.xlsx')

# Count the number of students for each event
event_counts = df['Events'].value_counts()

# Find the event with the most students
most_popular_event = event_counts.idxmax()

#print(event_counts)
print('The event that tends to attract more students is:',  most_popular_event)