import numpy as np
import pandas as pd

#creating table to test
"""
name_table = {'StudentID':  ['V001', 'V002', 'V003', 'V004', 'V005', 'V006'],
              'Name': ['Abe', 'Abhay', 'Acelin', 'Adelphos', 'Edward', 'Bob']}
              
name_table = pd.DataFrame(name_table)

print(name_table)
"""

name_table['Name'] = name_table.Name.str.lower()

name_table['Name'] = np.where(name_table.Name.str.contains('E'), name_table.Name.str.upper(), name_table.Name)

name_table['Name'] = np.where(name_table.Name.str.contains('e'), name_table.Name.str.upper(), name_table.Name)

print(name_table)
