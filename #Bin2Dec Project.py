#Bin2Dec Project

# Initial Variable Declarations
total = 0
index = 0

# Take in User Input and convert for processing
user_input = input("Please input 1 or more binary digits: ")
user_input_size = len(user_input)

# Presence Check
while user_input_size == 0:
    print("The input cannot be empty. Please input 1 or more binary digits: ")
    user_input = input("Please input 1 - 8 bit binary digits: ")
    user_input_size = len(user_input)

# Validity check
while index <= user_input_size - 1:
    if user_input[index] != "0" and user_input[index] != "1":
        print("The app can only convert binary digits. Please input 1 or more bit binary digits: ")
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
