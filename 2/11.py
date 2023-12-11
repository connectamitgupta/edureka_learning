'''.By using list comprehension, 
please write a program to print the list after removing the 
0th,4th,5th numbers in [12,24,35,70,88,120,155]'''

a=[12,24,35,70,88,120,155]
remloc=[0,4,5]
remval=[]
for i in remloc:
    remval.append(a[i])

# print(remval)
for x in remval:
    i=a.index(x)
    # print(i)
    a.pop(i)

print(a)