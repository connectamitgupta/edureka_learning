'''
Write a for loop that prints all elements of a list and their position in the list.
a = [4,7,3,2,5,9] 
Hint: Use Loop to iterate through list elements
'''

a = [4,7,3,2,5,9]

for p in a:
    # print(p)
    loct=a.index(p)
    print(f'At location {loct} value is {p}')
