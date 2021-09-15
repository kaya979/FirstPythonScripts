#Exercise 2:
#Create a new script.
#Ask the user of your script for a number. Give them a response based on whether the number is higher than, lower than, or equal to 100.
#Example output:


a = int(input("Enter a number: "))
b = 100

if a < b:
    print(a, ". That is lower than 100.")

elif a == b:
    print(a, "is a nice number")
else:
    print(a, ". That is a higher number than 100")


