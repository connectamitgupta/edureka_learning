'''Write a program, whichwill find all the numbers between 1000 and 3000 (both included) such that each digit of a number is an even number. The numbers obtained should be printed in a comma separated sequence on a single line.Hint: In case of input data being supplied to the question, it should be assumed to be a console input.Divide each digit with 2 and verify is it even or not.'''

print("*"*50)
print("Program to find even number between 1000 and 300 and each number is EVEN")
print("*"*50)
i=1000
j=3000
numbers=[]

for i in range(j):
    if i%2==0:
        numbers.append(str(i))
        numbers.append(",")

print(numbers)
str1 = " "
print(str1.join(numbers))
