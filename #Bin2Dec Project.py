#Bin2Dec Project

#Need to create and design window


# Initial Variable Declarations
total = 0
index = 0

# Take in User Input and convert for processing
user_input = input("Please input 1 - 8 bit binary digits: ")
user_input_size = len(user_input)

# Presence Check
while user_input_size == 0:
    print("The input cannot be empty. Please input a 1 - 8 bit binary digits: ")
    user_input = input("Please input 1 - 8 bit binary digits: ")
    user_input_size = len(user_input)

# Length check 
# PLEASE COMMENT THIS PART TO CONVERT MORE BINARY DIGITS (> 8) TO DENARY
while user_input_size > 8:
    print("The app can only convert up to 8 bits. Please input a 1 - 8 bit binary digits: ")
    user_input = input("Please input 1 - 8 bit binary digits: ")

# Validity check
while index <= user_input_size - 1:
    if user_input[index] != "0" and user_input[index] != "1":
        print("The app can only convert binary digits. Please input a 1 - 8 bit binary digits: ")
        user_input = input("Please input 1 - 8 bit binary digits: ")
        user_input_size = len(user_input)
        index = 0
    else:
        index += 1
    
# Convert input into an array
binary_input_array = list(user_input)
array_size = len(binary_input_array)

# Flip the array
binary_input_array.reverse()
    
# Program Logic   
for i in range(0, array_size):
    if binary_input_array[i] == '1':
        total += 2**i
    else:
        total += 0

print("The equivalent denary equivalent for", user_input, "is", total)
