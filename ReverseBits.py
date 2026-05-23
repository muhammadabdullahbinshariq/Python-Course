def Flip(num):
    bits = [] 
    temp = num 
    
    while (temp != 0): 
        divide = temp // 2 
        remainder = temp % 2 
        remainder = str(remainder) 
        bits.append(remainder) 
        temp = divide 
        
    bits.reverse() 
    bits = "".join(bits) 
    
    flip = [] 
    for i in bits: 
        if i == '0': 
            i = '1' 
            flip.append(str(i)) 
        else: 
            i = '0' 
            flip.append(str(i)) 
            
    flip = "".join(flip) 
    binary_str = flip 
    binary_list = list(binary_str) 
    length = len(binary_list) 
    length -= 1 
    updated = [] 
    
    for bit in binary_list: 
        bit_int = int(bit) 
        byte_value = bit_int * (2 ** length) 
        updated.append(byte_value) 
        length -= 1 
        
    print(f"\nOriginal Number : {num} ({bits})₂\nFlipped Number : {sum(updated)} ({flip})₂")

num = int(input("Enter an integer: "))
Flip(num)