import math
input_name = input("Choose a name : ")
studentsTuring = ["Redouane", "Justine", "Ruben", "Edouard"]

if(input_name in studentsTuring):
    print("Name is already used")
else:
    print('You can add the name in the array')
    
#other exercice count number of string in hello world


countAlpha = len("Hello Word")
print(countAlpha)

countFloat = float(countAlpha)
print(countFloat)

roundPi = math.pi

print("${:.3}".format(roundPi))

reversedText = 'Hello World'

print(list(reversedText))

age = input("What ur age ? ")
print(type(age) , age)

num = [2, 8, 1, 4, 6, 3, 7] 
sortNum = sum(num)
minNum = min(num)
maxNum = max(num)
print(sortNum, minNum, maxNum)

