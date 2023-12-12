'''Write a program that accepts a comma separated sequence of words as input and
prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
 without,hello,bag,world
 Then, the output should be:
 bag,hello,without,world
'''

inst=input("Please enter comma seperated string: ")
# inst="without,hello,bag,world"
# print(inst)
print(type(inst))
inst_list=inst.split(",")
inst_list.sort()
# print(inst_list)
print(type(inst_list))
print((',').join(inst_list))