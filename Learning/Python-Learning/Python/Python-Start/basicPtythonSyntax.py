age = 42
age += 10
divAge = 7
textDiv = age // divAge


# Calcul du reste de la division
restDiv = age % divAge

# Calcul de l'exposant de restDiv élevé à la puissance 3
expDiv = restDiv ** 3

print("{} divided by {} is equal {}".format(age,divAge,textDiv))
print("{} cubded is {}".format(restDiv, expDiv))

#Test du input()
# Il faut d'abord initialiser une variable avec l'input et puis print cet variable

testInput = input("Enter an integer : ")
print("You enter :", testInput)










