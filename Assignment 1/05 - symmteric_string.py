#Take string from user
string = input("Enter a string: ")
#Check if string is symmetric
stringLength = (len(string))
print(stringLength)
if string[:int(stringLength/2)] == string[int(stringLength/2):]:
    print("String is symmetric")
else:
    print("String is not symmetric")