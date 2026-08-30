import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Penguins Data.csv")
df = df.dropna()

male_df = df[df["Gender"] == "male"]
female_df = df[df["Gender"] == "female"]
labels = ["Male", "Female"]
colors = ["#2A9D8F", "#4C72B0"]

plt.figure()  
length_data = [male_df["Culmen Length (mm)"], female_df["Culmen Length (mm)"]]
length_bins = [30, 35, 40, 45, 50, 55, 60]

plt.hist(length_data, color=colors, bins=length_bins, label=labels)
plt.xlabel("Culmen Length (mm)")
plt.ylabel("Number of Penguins")
plt.title("Distribution of Culmen Length by Gender")
plt.legend()
plt.show()

plt.figure()
depth_data = [male_df["Culmen Depth (mm)"], female_df["Culmen Depth (mm)"]]
depth_bins = [13, 15, 17, 19, 21, 23] 

plt.hist(depth_data, color=colors, bins=depth_bins, label=labels)
plt.xlabel("Culmen Depth (mm)")
plt.ylabel("Number of Penguins")
plt.title("Distribution of Culmen Depth by Gender")
plt.legend()
plt.show()

plt.figure()
flipper_data = [male_df["Flipper Length (mm)"], female_df["Flipper Length (mm)"]]
flipper_bins = [30, 50, 70, 90, 110, 130] 

plt.hist(flipper_data, color=colors, bins=flipper_bins, label=labels)
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Number of Penguins")
plt.title("Distribution of Flipper Length by Gender")
plt.legend()
plt.show()

plt.figure()
mass_data = [male_df["Body Mass (g)"], female_df["Body Mass (g)"]]
mass_bins = [30, 50, 70, 90, 110, 130] 

plt.hist(mass_data, color=colors, bins=mass_bins, label=labels)
plt.xlabel("Body Mass (g)")
plt.ylabel("Number of Penguins")
plt.title("Distribution of Body Mass by Gender")
plt.legend()
plt.show()
