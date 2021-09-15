import random
print("Here are the rules: \n'Guess a number between 1 and 100.' \n'We'll give you a hint if you need one.'")
num = int(random.randint(1,100))
print(num)
guess_count = int(1)
guess = int(input("Guess a number! "))
orbit_greater = num + 10
orbit_less = num - 10
while guess != num:
    guess_count = guess_count + 1    
    if guess > num < orbit_greater:
        print("WARM")
    if guess < num > orbit_less:
        print("COLD")    
    if guess <= 0:
        print("Out of Bounds. Try again.")
    if guess > 100:
        print("Out of Bounds. Try again.")
    guess = int(input("Guess again: "))
if guess == num:
    print("You've won! It took you %d tries, but you got it. " % (guess_count))