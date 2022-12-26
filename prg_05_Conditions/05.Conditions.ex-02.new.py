# y needs to be guessed
# x is user input
# we create a loop, and it will continue if the input user is not y

print("Hey, let's play a guessing game, any number under 100:")
y = 100         
x = 0
while x != 100:                     # != means ; while x is not equal to 100:
    x = int(input("Input a number: "))      # ask the user for input
    if x == y:                              # if x is same as y, then shows "This is perfect"
        print (x, "is perfect")
    elif x < y:                             #if x is smaller than y, then shows "too low"
        print(x, "this number is too low!")
    elif x > y:                             #if x is bigger than y, then it shows "too high"
        print(x, "this number is too high")

