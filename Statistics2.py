import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""####**Import Dataset**"""

df = pd.read_csv("Weather Dataset.csv")
df.head(10)
df.info()

"""####**Check Null Values"""

df.isnull().sum()

"""**No feature has any null values"""

"""#### **Mean, Varience and Standard deviation of Temprature (C)**"""

mean_t = np.mean(df["Temperature (C)"])
print("Mean Temprature is :", mean_t)

var_t = np.var(df['Temperature (C)'])
print("Variation of Temprature is :", var_t)

standard = np.std(df['Temperature (C)'])
print("Standard Deviation of Temprature is :", standard)

"""#### **Mean, Variance and Standard Deviation of Teprature (C) for every month"""

for i in range(1, 13):
    month = df.loc[df["month"] == i]["Temperature (C)"]
    print("For month "+str(i))
    print("Mean temprature is "+ str(np.mean(month)))
    print("Standard Deviation is"+ str(np.std(month))+"\n")
