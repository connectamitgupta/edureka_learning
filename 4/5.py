'''Design a software for bank system. There should be options like cash withdraw,
cash credit and change password. According to user input, the software should
provide required output.
Hint: Use if else statements and functions.
'''


print("*"*50)
print(" "*10," Banking System "," "*10,)
print("*"*50)
print('''      1. Cash Withdraw
      2. Cash Deposit
      3. Chnage Password
      -------------------------------------------
      Select option from above''')
x=int(input("Select option from above: "))
if x==1:
    cw=int(input("Enter amount to withdraw: "))
    if cw<=1:
        print("Please enter correct amount")
    else:
        print("Amount {0} withdrawl successfully!".format(str(cw)))

elif x==2:
    cd=int(input("Enter amount to deposit: "))
    if cd<=1:
        print("Please enter correct amount")
    else:
        print(f"Amount {cd} deposited successfully!")

elif x==3:
    cp=input("Enter new password: ")
    print("Password changed successfully!")
else:
    print("Invalid option chosen")
