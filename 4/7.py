'''Write a program which can compute the factorial of a given numbers. Use recursion to find it.
Hint: Suppose the following input is supplied to the program: 8 Then, the output should be:40320
'''
p=int(input("Enter number to find factoral: "))
k=1
for i in range(p,k,-1):
    k=k*i

print(k)