'''Write  a  program  to  compute  1/2+2/3+3/4+...+n/n+1  with  a  given  n  input  by console (n>0)'''

a=int(input("Enter length of list: "))
if a<2:
    print("Please enter valid number")
else:   
    b=[]
    # i=1
    for i in range(a):
        b.append(i*2)

    print(b)
