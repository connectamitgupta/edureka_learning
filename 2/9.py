'''With a given list [12,24,35,24,88,120,155,88,120,155], 
write a program to print this list after removing all duplicate values with original order reserved'''
a=[12,24,35,24,88,120,155,88,120,155]
print(f'Given list is :{a} and number of element are : {len(a)}')

print('Now removing duplicate values....')
b=set(a)
print(f"Removed {len(a)-len(b)}...unique elements now...{len(b)}")
print(list(b))