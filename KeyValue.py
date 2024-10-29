'''
 The program takes a key-value pair and adds it to the dictionary. 
Problem Solution:
1. Take a key-value pair from the user and store it in separate variables.
2. Declare a dictionary and initialize it to an empty dictionary.
3. Use the update() function to add the key-value pair to the dictionary.
4. Print the final dictionary.
5. Exit.
Sample I/O:
12
34
Sample o/p:
{12: 34}
'''
# Step 1: Take a key-value pair from the user
key = input("Enter the key: ")
value = input("Enter the value: ")

# Step 2: Declare an empty dictionary
my_dict = {}

# Step 3: Use the update() function to add the key-value pair to the dictionary
my_dict.update({key: value})

# Step 4: Print the final dictionary
print(my_dict)

# Step 5: Exit (this is implicit in Python, as the program will end here)
