'''Design a code which will find the given number is Palindrome number or not.Hint: Use built-in functions of string.'''
'''Created by Amit Gupta, Contact: 9214800120'''
'''Regarding python assignment for edureka'''

xStr=input("Enter number to check: ")
y=xStr[::-1]
if y==xStr:
    print("These are palindrome numbers")
else:
    print("These are not palindrome numbers")