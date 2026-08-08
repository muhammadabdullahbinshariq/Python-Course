import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')
df = df.dropna()

print("--- First 5 rows of 'tips' dataframe ---")
print(df.head())
print()
print("--- Information regarding 'tips' dataframe ---")
print(df.info())
print()
print("--- Describing 'tips' dataframe ---")
print(df.describe())

sns.barplot(data = df, x = 'day', y = 'total_bill', hue = 'sex')
plt.xlabel("Days")
plt.ylabel("Total Bill")
plt.title("Average Total Bill")
plt.show()

sns.countplot(data = df, x = 'day', hue = 'sex')
plt.ylabel("Count")
plt.xlabel("Day")
plt.title("Bill Paid by Which Sex")
plt.show()

sns.boxplot(data = df, x = 'day', y = 'total_bill')
plt.xlabel("Days")
plt.ylabel("Total Bill")
plt.title("Spread of Bills")
plt.show()

sns.stripplot(data = df, x = 'day', y = 'total_bill', jitter = True, hue = 'size')
plt.xlabel("Days")
plt.ylabel("Total Bill")
plt.title("All Bills")
plt.show()


sns.swarmplot(data = df, x = 'day', y = 'total_bill', hue = 'size')
plt.xlabel("Days")
plt.ylabel("Total Bill")
plt.title("All Bills")
plt.show()

sns.jointplot(data = df, x = 'total_bill', y = 'tip', hue = 'sex')
plt.ylabel("Tip")
plt.xlabel("Total Bill")
plt.suptitle("Relation Between Bills and Tips", y = 1.02)
plt.show()


sns.jointplot(data = df, x = 'total_bill', y = 'tip', kind = 'kde')
plt.ylabel("Tip")
plt.xlabel("Total Bill")
plt.suptitle("Relation Between Bills and Tips", y = 1.02)
plt.show()

sns.pairplot(df[['total_bill', 'tip', 'size']])
plt.suptitle('Pair Plot Bill, Tip and Size', y = 1.02 )
plt.show()

sns.pointplot(data = df, x = 'day', y = 'total_bill', hue = 'sex')
plt.xlabel("Days")
plt.ylabel("Total Bill")
plt.title("Average Total Bill")
plt.show()

sns.lmplot(data = df, x = 'total_bill', y = 'tip')
plt.ylabel("Tip")
plt.xlabel("Total Bill")
plt.suptitle("Relation Between Bills and Tips", y = 1.02)
plt.show()
