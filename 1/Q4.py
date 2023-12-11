'''Write a program that accepts a sentence and calculate the number of letters and digits.Suppose if the entered string is: Python0325Then the output will be:LETTERS: 6DIGITS:4Hint: Use built-in functions of string.'''

print("*"*50)
print("program to accepts a sentence and calculate the number of letters and digits")
print("*"*50)

strX=input("Enter alphanumeric string to check: ")

digit=letter=0
strLen=len(strX)
print("Total Length is :",strLen)

for x in strX:
    if x.isdigit():
        digit+=1
    
    if x.isalpha():
        letter+=1

print(f"No. of digit are {digit} and letters are {letter}")