'''Data of XYZ company is stored in sorted list. Write a program for searching
specific data from that list.
Hint: Use if/elif to deal with conditions'''


xyzcompanydata=['book','pencil','pen','note book','sharpener','rubber']
item = input ("What item do you want to Search: ")
for i in range(1):
    if item in xyzcompanydata:
        print("Item is in company data")
        break 
    else:
        print("data is not available")