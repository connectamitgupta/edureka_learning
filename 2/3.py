'''A website requires a user to input username and password to register. 
Write a program to check the validity of password given by user. 
Following are the criteria for checking password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
3. At least 1 letter between [A-Z]
4. At least 1 character from [$#@]
5. Minimum length of transaction password: 6
6. Maximum length of transaction password: 12
Hint: In case of input data being suppliedto the question, it should be assumed to be a console input'''


psswrd = input("Enter valid password: ")
p1=len(psswrd)
r1=r2=r3=r4=r5=r6=0
sp=['$','@','#']
if (p1>6) and (p1<=12):
    r5=r6=1

# if p1>12:
#     r6=0

for x in psswrd:
    if x.isdigit():
        r2=1
    
    if x.isalpha():
        if x.isupper():
            r3=1
        elif x.islower():
            r1=1
    if x in sp:
            r4=1

r=r1+r2+r3+r4+r5+r6
if r==6:
     print("Valid Password, Well Done")
else:
     print("Invalid Password Retry")