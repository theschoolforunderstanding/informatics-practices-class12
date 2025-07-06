# EXAMPLE 8
# Write a program to create a Series object using
# a dictionary that stores the number of students in
# each section of class 12 in your school.

#SOLUTION
import pandas as pd
stu = { 'A': 39, 'B': 41, 'C': 42, 'D': 44 }
s8 = pd.Series(stu)
print(s8)
