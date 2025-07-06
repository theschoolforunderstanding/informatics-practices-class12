# EXAMPLE 8
# Write a program to create a Series object
# that stores the initial budget allocated (50000)
# – each for the four quarters of the
#year: Qtr1, Qtr2, Qtr3, Qtr4.

#SOLUTION
import pandas as pd
s9 = pd.Series(50000, index=['Qtr1', 'Qtr2', 'Qtr3', 'Qtr4'])
print(s9)

