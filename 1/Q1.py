#### Program to check number given is even or odd ##############

print("*******************  Program to check Even or ODD Check  ***************************")
while True:
    x=int(input("Enter Number:  "))
    rem=x%2
    print(rem)
    if rem is 0:
        print("This is Even number")
    else:
        print("This is ODD number")