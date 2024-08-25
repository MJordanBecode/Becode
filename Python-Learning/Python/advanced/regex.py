#import regex module "re"

import re

pattern='[ ]'
string ='I am fine ! There are still 6 months left :()'

#Cut the string according to the occurrence of the pattern.
print(re.split(pattern, string))


pattern="GR(.)?Y"
string="GREY"

result = re.match(pattern, string)
print(result)

# It is equals to
prog = re.compile(pattern)
result = prog.match(string)
print(result)

#  So in a loop the second syntax is nice
pattern="GR(.)?Y"
prog = re.compile(pattern)
l=["GREY 'S","GRAY","GREYISH","A GREY"]
for elem in l:
    result = prog.match(elem)
    print(elem,result)
    
    
# Only numbers
print(re.findall("([0-9]+)", "Hello I live on the 7th floor of 220 street of 236 sims"))
# "+" Means 1 or more characters

# Only words
print(re.findall("([A-z]+)", "Hello I live on the 7th floor of 220 street of sims"))

nb = input('Your number : ')
if (re.match("^[0-9]+$", nb)): #verify is the input enter is a number start to 0 and end to 9
    print("The string entered is a number.")
else:
    print("The string entered is NOT a number")


rog = re.compile("^[0-9]+$")
if  prog.search(nb) is not None : 
    print("The string entered is a number.")
else:
    print("The string entered is NOT a number")