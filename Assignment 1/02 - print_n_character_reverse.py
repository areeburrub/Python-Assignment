#Take a string from user
string = input("Enter a string: ")
#Take n from user
n = int(input("Enter n: "))
#Print the last n characters of the string
print("Last", n, "characters of the string are: ", string[-n:])