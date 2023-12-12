'''Write a program which accepts a sequence of comma separated 4 digit binary
numbers as its input and then check whether they are divisible by 5 or not. The
numbers that are divisible by 5 are to be printed in a comma separated sequence
'''

# Create an empty list named 'items'
items = []

# Take user input and split it into a list of strings using ',' as the delimiter
num = [x for x in input("Enter number: ").split(',')]

# Iterate through each element 'p' in the 'num' list
for p in num:
    # Convert the binary string 'p' to its decimal equivalent 'x'
    x = int(p, 2)
    
    # Check if 'x' is divisible by 5 (i.e., when divided by 5 there's no remainder)
    if not x % 5:
        # If 'x' is divisible by 5, add the binary string 'p' to the 'items' list
        items.append(p)

# Join the elements in the 'items' list separated by ',' and print the result
print(','.join(items))