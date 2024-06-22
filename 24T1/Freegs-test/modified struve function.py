import numpy as np
from scipy.special import modstruve
from scipy.special import struve
import csv
import pandas as pd


k = pd.read_csv('k and L-1.csv',     # Read first pandas DataFrame column
                           usecols = [0], index_col=False)


L = (modstruve(-1, k))

L.to_csv('k and L-1.csv', index=False)

print(modstruve(-1,0.974940125))
print(struve(-1, 0.974940125))
#with open('test.csv', "w",newline='') as f:
   # writer = csv.writer(f)
   # for row in rows:
   #     writer.writerow(row)
