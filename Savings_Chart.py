import matplotlib.pyplot as plt

x = ["Week1", "Week2", "Week3", "Week4", "Week5", "Week6"]
y = [250, 340, 190, 230, 300, 200]

plt.xlabel("Weeks")
plt.ylabel("Savings ($)")
plt.title("Savings Line Graph")
plt.plot(x, y, marker = "o", color = "#04D9FF", linestyle = "dashed")
plt.grid(True)
plt.show()

plt.xlabel("Weeks")
plt.ylabel("Savings ($)")
plt.title("Savings Line Graph")
plt.bar(x, y)
plt.grid(True)
plt.show()