"""
Rename Columns
Input parameters
pandas.DataFrame object
sequence
Task
Your function must return a new pandas.DataFrame object with same data than the original input but now its column names are the elements of the sequence. You must not modify the original input.

The number of columns of the input will always be equal to the size of the sequence.

Examples
   0  1  2
0  1  2  3
1  4  5  6

names = ['A', 'B', 'C']
   A  B  C
0  1  2  3
1  4  5  6
"""

import pandas as pd

def rename_columns(df, names):  
    return df.rename(columns=dict(zip(df.columns, names)))

print(rename_columns(pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'C' : [5, 6]}), ['A', 'B', 'C']))