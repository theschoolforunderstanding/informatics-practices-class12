# EXAMPLE 7
# Write a program to create a Series object using an
# ndarray that is created by tiling a list [3, 5] twice.

#SOLUTION
import pandas as pd
import numpy as np
s7 = pd.Series(np.tile([3, 5], 2))
print(s7)
