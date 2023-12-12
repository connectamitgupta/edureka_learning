'''Write a program that accepts sequence of lines as input and prints the lines after
making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
 Hello world
 Practice makes perfect
 Then, the output should be:
 HELLO WORLD
 PRACTICE MAKES PERFECT'''

print("Enter Sentence continue and when you are done enter Q to stop and print output")
alist=[]
while True:
    a=input("Enter Sentence: ")
    if a=="Q":
        print((',').join(alist))
        break
    else:
        alist.append(a.upper())