#Take input from user
num = int(input("Enter a number: "))
#Initialize reverse to 0
reverse = 0
#Loop until num is 0
while num > 0:
    #Get the last digit of num and add it to reverse
    reverse = reverse * 10 + num % 10
    #Remove the last digit from num
    num = num // 10
#Print the reverse
print("Reverse of the number is: ", reverse)