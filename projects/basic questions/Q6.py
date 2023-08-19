# Q6. How does the GPA vary amoung different collages? (show top 5 results only)

import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the Excel file
df = pd.read_excel(r'S:\projects\basic questions\Data analyst Data.xlsx')

# Group the data by College Name and calculate the mean and standard deviation of CGPA for each College Name
CGPA_stats = df.groupby('College Name')['CGPA'].agg(['mean', 'std'])

# Sort the data by mean CGPA in descending order and select the top 5 College Names
top_5 = CGPA_stats.sort_values(by='mean', ascending=False).head(5)

# Plot the mean and standard deviation of CGPA for the top 5 College Names
top_5.plot(kind='bar', y=['mean', 'std'], rot=0)
plt.xlabel('College Name')
plt.ylabel('CGPA')
plt.title('Top 5 College Names by Mean CGPA')
plt.show()
