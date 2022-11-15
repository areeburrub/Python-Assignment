#Take a string from user
string = input("Enter a string: ")
#Separate words from the string
words = string.split()
#Print the first two characters of all words
print("First two characters of all words are: ", end="")
for word in words:
    print(word[:2], end=" ")