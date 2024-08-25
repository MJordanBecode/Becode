name = "Alan Turing"
age = 17
person = [name, age, "mathematician"]

typeage = type(age)
print("Hello, my name is {} and I am {} years old and I am a {}".format(person[0], person[1], person[2]))
print(typeage)

a  = 4
b = 12

floorDiv = b // a
print(floorDiv)

x = 2
print(x == 2)
print(x ==3)
print(x < 3)

if age >=18:
    print("You're an adult!")
elif age < 18:
    print("You're younger than adulte")
    
    
student1 = "John"
student2 = "Eric"

if student1 == "John" and student2 == "Eric":
    print("You are John AND Eric")   
else :
    print("Welcome anonymous")