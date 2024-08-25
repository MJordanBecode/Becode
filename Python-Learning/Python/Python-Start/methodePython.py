txt = "hello, and welcome to my world."
capitalizeTxt = txt.capitalize()
print(capitalizeTxt) 

a = 10 # Creating the int() instance
y = 11
print(id(a), id(y))
print(a is y) # comparing the types



person = ["James", "Bond", "007", "Secret agent"]
person2 = person
person3 = person
print(id(person), id(person))

person += ["English"]
person2 += ["Man"]
person3 += ["test"]
print(id(person),id(person2))
print(person, person2)

name = {}
name["firstName"] =  "Alan"
name["lastName"] = "Turing"
name["test"] = 'test'

def hello(firstName, lastName, test):
    print("Hello {} {} {} and welcome".format(firstName, lastName, test)) 
    
hello(**name)

def multiply(*elements): # Add "*" to indicate that the parameters are infinite
    res = 1
    for element in elements:
        res = res * element
        print(res)
    return res
multiply(1,2,3,4,5,6,7,8,9,10)