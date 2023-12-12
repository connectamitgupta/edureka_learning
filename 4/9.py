'''Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional
array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡-Y-1.
Example:
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
'''

row_num=int(input("Enter first number: "))
col_num=int(input("Enter second number: "))
if col_num<=row_num:
    print("Please enter bigger number")
    exit()

multi_list = [[0 for col in range(col_num)] for row in range(row_num)]
print(multi_list) 

# Nested loop to populate the 2D list with multiplication results
for row in range(row_num):
    for col in range(col_num):
        # Set the value at position [row][col] in the 2D list to the product of 'row' and 'col'
        multi_list[row][col] = row * col

# Print the resulting 2D list containing the multiplication table
print(multi_list)