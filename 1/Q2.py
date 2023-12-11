#'''""Write a code which accepts a sequence of words as input and prints
# the words in a sequence after sorting them alphabetically. Hint: In case of input data being supplied to the question, it should be assumed to be a console input.''''''

print('*'*50)
print('*********** Program to Sort alphabetcally ascending given string *************')
x1=input('Enter string:  ')
l=len(x1)
print('Length of this string is ',l)

# converting the string into a list of words
words = [word.lower() for word in x1.split()]

# sort the words in list
words.sort()
print(words)

# display sorted words efficiently
print("The sorted words are:")
for word in words:
   print(word)