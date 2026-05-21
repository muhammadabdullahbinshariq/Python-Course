binary_str = input("Enter a Binary code: ")
binary_list = list(binary_str)
length = len(binary_list)
length -= 1

updated = []

for bit in binary_list:
    bit_int = int(bit)
    byte_value = bit_int * (2 ** length)
    updated.append(byte_value)
    length -= 1

print("Positional values:", updated)
print("Decimal Total:", sum(updated))