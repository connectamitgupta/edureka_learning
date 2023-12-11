'''By using list comprehension, 
please write a program to print the list 
after removing the value 24 in [12,24,35,24,88,120,155]'''

a=[12,24,35,24,88,120,155]
i=0
l=len(a)
while i<=l:
    p=a.index(24)
    print(p)
    a.pop(p)
    print(a)