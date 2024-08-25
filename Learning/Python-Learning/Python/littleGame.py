class CreatePerso:
    def __init__(self, firstname, lastname, race):
        self.firstname = firstname
        self.lastname = lastname
        self.race = race
        self.lvl = 0
        self.hp = 100
        self.shield = 0
        self.skill = "Punch"

        # Initialisation des attributs avec des valeurs par défaut
        self.strength = 10
        self.dexterity = 10
        self.constitution = 10
        self.intelligence = 10
        self.wisdom = 10
        self.charisma = 10

    def __str__(self):
        return "I'm {} {} and I'm an {}".format(self.firstname, self.lastname, self.race)
    
    def attributes_perso(self):
        return """strength = {} 
                  dexterity = {} 
                  constitution = {} 
                  intelligence = {} 
                  wisdom = {} 
                  charisma = {}""".format(
                      self.strength, self.dexterity, self.constitution,
                      self.intelligence, self.wisdom, self.charisma
                  )

# Create an instance of CreatePerso with default attributes
test = CreatePerso("John", "Doe", "Elf")

# Print character description
print(test)

# Print character attributes with default values
print(test.attributes_perso())
