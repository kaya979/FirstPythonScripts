# Create a new script.
# Use user input to ask for their information (first name, last name, job title, company). 
# Store the information in a dictionary.

# Write the information to a csv file (comma-separated values). 
# The data should not be overwritten when you run the script multiple times.

a = input("enter your first name:")
b = input("enter your last name:")
c = input("enter your job title:")
d = input("enter your company name:")

thisdict = {
    "First Name:":a,
    "Last Name:":b,
    "Job Title:":c,
    "Company:":d,



}
print("-------------------------------------")
print(thisdict)
for key, value in thisdict.items():
    print(key,  ':',    value)
print("-------------------------------------")

