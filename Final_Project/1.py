'''Create a python script called googlesearch that provides a command line utility to
perform google search. It gives you the top links (search results) of whatever you want to
search on google.
'''

try:
    from googlesearch import search
except ImportError: 
    print("No module named 'google' found")
 
# to search
# query = "Geeksforgeeks"
query=input("Enter string to search from Google: ")

for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(j)