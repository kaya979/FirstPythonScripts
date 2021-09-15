#Create a new script.
#Use the input() function to get input from the user. 
# Store that input in a variable.
#Find out what data type the output of input() is. 
# See if it is different for different kinds of input (numbers, words, etc.).

x = input("Hi, what is your name?:")         #here we use the 'input' function so that the user can fill in characters
y = input('Input your age:')                   #here the user enters his age
print('Hello, ' + x)                        #here we print out the message "Hello with the input of the first question"
print('You are '+ y + ' years old.')            #here we print out the message You are ....years old including the input of 2nd question

# or

print('Hello ' + x + ". You are " + y + " years old. ")
print("this is data type", type(x))
print("this is data type", type(y))

