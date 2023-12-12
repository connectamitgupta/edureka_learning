'''Write a program which will find all such numbers which are divisible by 7 but are
not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained
should be printed in a comma-separated sequence on a single line.
'''
bnum=2000
enum=3200
cslist=[]
for i in range(bnum,enum):
    if i%7==0:
        if i%5 is not 0:
            cslist.append(i)

print(f"No. of members {len(cslist)} found {cslist}")