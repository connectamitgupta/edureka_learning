'''2.Write a program that accepts a sequence of whitespace separated words as input
and prints the words after removing all duplicate words and sorting them
alphanumerically.
Suppose the following input is supplied to the program:
 hello world and practice makes perfect and hello world again
 Then, the output should be:
 again and hello makes perfect practice world
'''

inst=input("Please enter string seperated by white space: ")
# inst="without,hello,bag,world"
# print(inst)
print(type(inst))
inst_list=inst.split(" ")

inst_list_unique=[]
for a in inst_list:
    if a not in inst_list_unique:
        inst_list_unique.append(a)
    
inst_list_unique.sort()
# print(inst_list)
print(type(inst_list_unique))
# inst_set=set(inst_list)
print((' ').join(inst_list_unique))