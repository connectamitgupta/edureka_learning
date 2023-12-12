import os

print(os.getcwd())
d1=os.getcwd()
d2=os.mkdir(d1+'test')
print(d2)
print(os.name)
# print(os.environ)
print(os.getlogin())
print(os.getppid())