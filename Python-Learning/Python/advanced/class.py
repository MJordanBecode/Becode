# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

    # instance method
    def is_hungry(self, hungry):
        if hungry < 0:
            # Affiche un message pour dire qu'il est affamé et qu'il faut le nourrir
            print("He is hungry, feed him")
        else:
            # Retourne un message pour dire qu'il est rassasié
            return "He is fed"

# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# Création d'une instance de RussellTerrier
russell = RussellTerrier(name="Jack", age=5)

# Création d'une instance de Bulldog
bulldog = Bulldog(name="Buddy", age=3)

# Affichage des informations pour RussellTerrier
print(russell.description())  # Affiche: Jack is 5 years old
print(russell.speak("Woof"))  # Affiche: Jack says Woof
print(russell.run("fast"))    # Affiche: Jack runs fast
print(russell.is_hungry(-3))  # Affiche: He is hungry, feed him

# Affichage des informations pour Bulldog
print(bulldog.description())  # Affiche: Buddy is 3 years old
print(bulldog.speak("Ruff"))  # Affiche: Buddy says Ruff
print(bulldog.run("slow"))    # Affiche: Buddy runs slow
print(bulldog.is_hungry(5))