# Key-value pairs
# Key-value pairs are a general concept you will definitely encounter. 
# Some examples of where you will find them are NoSQL databases or AWS resource tags. 
# Dictionaries (dict) in Python also use key-value pairs to store information.
# Dicts in Python are written using curly brackets {}. 
# You can get values from the dict by calling its key. 


thisdict = {
    "First Name":"Coen",
    "Last Name":"Meulenkamp",
    "Job Title":"Learning Coach",
    "Company":"Techgrounds"

}

print(thisdict)
print("==========this will print out only once================")

for key, value in thisdict.items():
    print(key,  ':',    value)
    print("-------this line will loop until end----------")

print(".......end of message.................")
