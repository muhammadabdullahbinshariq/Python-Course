def bit_probe(number, position):
    return (number >> position) & 1

def get_subset(items, mask):
    subset = []
    for i in range(len(items)):
        if bit_probe(mask, i):
            subset.append(items[i])
    return subset

def generate_power_set(items):
    power_set = []
    n = len(items)
    for mask in range(1 << n):
        subset = get_subset(items, mask)
        power_set.append(subset)
    return power_set

def count_bit_difference(num1, num2):
    xor_result = num1 ^ num2
    difference = 0
    while xor_result > 0:
        difference += xor_result & 1
        xor_result >>= 1
    return difference

elements = ["A", "B", "C"]

print("--- Bit Probing Example ---")
print(f"Bit at position 0 of 5 (101 binary): {bit_probe(5, 0)}")
print(f"Bit at position 1 of 5 (101 binary): {bit_probe(5, 1)}")

print("\n--- Generating All Subsets (Two Loops) ---")
all_subsets = generate_power_set(elements)
for subset in all_subsets:
    print(subset)

print("\n--- Bit Difference Example ---")
number_a = 5  
number_b = 6  
diff = count_bit_difference(number_a, number_b)
print(f"Bit difference between {number_a} and {number_b}: {diff}")