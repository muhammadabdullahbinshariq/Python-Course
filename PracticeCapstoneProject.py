# Practice Capstone Project

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_id = '1ZIMKkik1Bjdo3qeXAIE7VrI9XMP1gZ-S'
direct_download_url = f'https://drive.google.com/uc?id={file_id}&export=download'
df = pd.read_csv(direct_download_url)

print("First 3 rows of IMDB Dataset:")
print(df.head(3))
print()
print("Last 3 rows of IMDB Dataset:")
print(df.tail(3))
print()
print("Describing IMDB Dataset:")
print(df.describe())
print()
print("Information regarding IMDB Dataset:")
print(df.info())
print()
print("Number of null values in IMDB Dataset:")
print(df.isnull().sum())
print()
subset = df.iloc[41 : 76]
print("Rows 41 to 75:")
print(subset)
print()
votes = df[df['No_of_Votes'] == max(df['No_of_Votes'])]
print("Higest Number of Votes:")
print(votes)

sns.boxplot(data = df, x = 'IMDB_Rating', y = 'Runtime')
plt.title('Rating per Time Run')
plt.ylabel('Time Run')
plt.xlabel('Rating')
plt.show()

corr = df[['IMDB_Rating', 'Runtime']].corr()
sns.heatmap(data=corr, annot=True, cmap='coolwarm')
plt.title('Correlation')
plt.show()

sns.jointplot(data = df, x = 'IMDB_Rating', y = 'Runtime', kind = 'hex')
plt.title('Rating per Time Run')
plt.ylabel('Time Run')
plt.xlabel('Rating')
plt.show()

sns.countplot(data = df, x = 'IMDB_Rating')
plt.title('Count of Movies With Particular Rating')
plt.ylabel('Count')
plt.xlabel('Rating')
plt.show()
