'''Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H: C is 50. H is 30.
D is the variable whose values should be input to your program in a commaseparated sequence.
 Example:
Let us assume the following comma separated input sequence is given to the
program:
100,150,180
The output of the program should be:
18,22,24

'''

import math
commaSepStr=input("Enter numbers seperated by comma: ")
dlist = commaSepStr.split(",")
print(dlist)
c=50
h=30
anslist=[]
for d in dlist:
    ansele=math.sqrt((c*int(d)*2)/h)
    anslist.append(int(ansele))

print("Answer is: ",anslist)