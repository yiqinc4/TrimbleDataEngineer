import numpy as np
import pandas as pd

#creating table to test
"""
name_table = {'StudentID': ['V001', 'V002', 'V003', 'V004', 'V005', 'V006'],
              'Name': ['Abe', 'Abhay', 'Acelin', 'Adelphos', 'Edward','Bob']}
              
name_table = pd.DataFrame(name_table)

mark_table = {'StudentID': ['V001', 'V002', 'V003', 'V004', 'V005', 'V006'],
              'Total_marks': [95, 80, 74, 81, 10, 30]}
              
mark_table = pd.DataFrame(mark_table)


print(name_table)

# Q1-b)
name_table['Name'] = name_table.Name.str.lower()

name_table['Name'] = np.where(name_table.Name.str.contains('E'), name_table.Name.str.upper(), name_table.Name)

name_table['Name'] = np.where(name_table.Name.str.contains('e'), name_table.Name.str.upper(), name_table.Name)

print(name_table)
"""

#Q1-c)

combined = pd.merge(name_table, mark_table, on='StudentID')

upper = combined[combined['Name'].str.isupper()]

lower = combined[combined['Name'].str.islower()]

name_avg = {'UpperCaseNameAVG': [upper['Total_marks'].mean()],
            'LowerCaseNameAVG': [lower['Total_marks'].mean()]}

name_avg = pd.DataFrame(name_avg)

print(name_avg)






