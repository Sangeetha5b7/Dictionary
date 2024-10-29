'''
The program takes a dictionary and prints the sum of all the items in the dictionary.
Problem Solution:
1. Declare and initialize the n number of dictionary values from the user.
2. Find the sum of all the values in the dictionary.
3. Print the total sum.
4. Exit.
Sample Input:
3
100
540
239
Sample Output :
879
'''
# Step 1: Declare and initialize the n number of dictionary values from the user
n = int(input("Enter the number of items in the dictionary: "))
my_dict = {}

for i in range(n):
    key = input(f"Enter key {i + 1}: ")
    value = int(input(f"Enter value for key {key}: "))  # Convert value to integer
    my_dict[key] = value

# Step 2: Find the sum of all the values in the dictionary
total_sum = sum(my_dict.values())

# Step 3: Print the total sum
print("Total sum of all values:", total_sum)

# Step 4: Exit (implicit)
