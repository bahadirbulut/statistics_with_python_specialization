import numpy as np
import pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("nhanes_2015_2016.csv")
# df = df.dropna()

# What is the median of NHANES BPXSY2
print("Median: {}".format(df.BPXSY2.median()))

# What is the mean
print("Mean: {}".format(round(df.BPXSY2.mean(), 1)))

# What is the sd
print("STD: {}".format(round(df.BPXSY2.std(), 1)))

# What is the max
print("Max: {}".format(round(df.BPXSY2.max(), 1)))

# What is the max
print("IQR: {}".format(round(stats.iqr(df.BPXSY2), 1)))
print(np.percentile(df.BPXSY2, 75))
print(np.percentile(df.BPXSY2, 25))

# Which of these will return desc stats for numeric Series
print(df.BPXSY2.describe())

# Which will produce hist of series
# sns.distplot(a=df.BPXSY2).set(title="Hist")
# plt.hist(df.BPXSY2)
# plt.show()

# How many rows displayed with df.head()
print(len(df.head()))

# What data is shown when df.head(2) code is run
print(df.head(2))




