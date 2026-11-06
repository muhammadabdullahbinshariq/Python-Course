import numpy as np

o_array = np.arange(10)
print(f"Original array : {o_array}")

m_array = np.where(o_array % 2 != 0, -1, o_array)
print(f"Modified (-1) array : {m_array}")

r_array = o_array.reshape(2, 5)
print(f"Reshaped array : {r_array}")

print("Sum of all even numbers using two methods:")

print("Method 1:")
s_array = np.where(o_array % 2 == 0)
print(f"Original array's even numbers : {s_array}")
print(f"Sum : {np.sum(s_array)}")

print("Method 2:")
f_list = []
for i in o_array:
    if i % 2 == 0:
        f_list.append(i)
print(f"Original array's even numbers : {f_list}")
print(f"Sum : {sum(f_list)}")