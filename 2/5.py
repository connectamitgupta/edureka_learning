'''Please   write   a   program   which accepts  a   string   from   console   
and   print   the characters that have even indexes.
Example: If the following string is given as input to the program:
H1e2l3l4o5w6o7r8l9d
Then, the output of the program should be:
Helloworld'''

xStr= input("Enter string with index to validate pattern: ")

for i in xStr:
    # print(f"value of i is: {i}")
    loc=xStr.index(i)
    # print(f"current location is: {loc}")
    if loc%2==0:
        if i.isalpha():
            # print(xStr[loc-1])
            print(i)
