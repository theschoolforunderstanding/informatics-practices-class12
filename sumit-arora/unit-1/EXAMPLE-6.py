# EXAMPLE 6
# Write a program to create a Series object using an
# ndarray that has 5 elements in the range 24 to 64.

#SOLUTION
import pandas as pd
import numpy as np
s6 = pd.Series(np.linspace(24, 64, 5))
print(s6)
