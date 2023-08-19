import pandas as pd

# Load the data from the Excel file
df = pd.read_excel('S:\projects\moderate questions\Data analyst Data.xlsx')

# Count the number of students for each PROMOTION
promotion_counts = df['How did you come to know about this event?'].value_counts()

# Find the event with the most students
most_popular_event = promotion_counts.idxmax()

#print(promotion_counts)
print('The promoyion channel that tends to attract more students is:',  most_popular_event)