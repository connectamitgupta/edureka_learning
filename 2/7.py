'''Please write a program which count 
and print the numbers of each character in a string input by console.
Example: If the following string is given as input to the program:abcdefgabc
Then, the output of the program should be:a,2c,2b,2e,1d,1g,1f,1'''

xStr=input("Enter string to count no of characters: ")

# initialize new list here
lst1 = []
for char in xStr:
    if char not in lst1:
        lst1.append(char)

# check each list item prence in string 
for item in lst1:
    print(item,xStr.count(item), sep = " exists number of times :")