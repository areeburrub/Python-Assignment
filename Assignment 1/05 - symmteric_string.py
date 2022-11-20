#Take string from user
string = input("Enter a string: ")
#Check if string is symmetric
if string == string[::-1]:
    print("String is symmetric")
else:
    print("String is not symmetric")