# EXAMPLE 8
# Write code to create a Series object that stores
# 200 medals for games to be held every alternate
# year in the decade 2020–2029.

#SOLUTION
import pandas as pd
stu = { 'A': 39, 'B': 41, 'C': 42, 'D': 44 }
s8 = pd.Series(stu)
print(s8)
