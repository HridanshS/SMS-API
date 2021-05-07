import pandas as pd
import numpy as np
#Insert complete path to the excel file and index of the worksheet
df = pd.read_excel("/Users/Shared/cs130R/message.py/file_name.xlsx", engine= 'openpyxl',sheet_name=0)
# insert the name of the column as a string in brackets
list1 = list(df['Name']) 
list2 =list(df['Phone'])


print(list1)
print(list2)
