import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#adds data to the dataframe and
#fills NaN's with 0's to prevent Nan problems
df = pd.read_excel('data/gti_2012-2021.xlsx')
df.fillna(float(0),inplace=True)

#filters down all the int/float dtyped series and
#replaces the dtype with float16 to save space, 135.4KB
#replaces 0 with NaN values to stop int0 statistical interference
y = [x for x in ((df.dtypes == int) |
                 (df.dtypes == float))]
y = df.dtypes.index[y] 
df[y[:3]] = df[y[:3]].astype('int8')
df[y[3:]] = df[y[3:]].astype('float16')
df[y[3:]].replace(0,np.NaN, inplace=True)
print(df.isna().any())