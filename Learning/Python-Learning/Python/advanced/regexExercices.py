#import module
import re

nb = input("Choose a number : ")

if(re.match("^[0-9]+$", nb)):
    print("The string entered is a number")
elif nb.startswith('-'):
    print("The string entered is negatif number : {}".format(nb))
else:
    print("The string entered is not a number")
    



# Exemple de chaînes à tester
tests = ["123", "-456", "0", "007", "12345678901234567890", "-1234567890", "abc", "12.34"]
tests2 = ["Je suis le meilleur car j'ai 23 ans et j'adore l'année 2024"]
pattern = r"(\d{2}) .* (\d{4})"

# Expression régulière pour trouver des entiers (positifs ou négatifs)
motif = r'^-?\d+$'

for test in tests:
    if re.match(motif, test):
        print(f"'{test}' est un entier.")
    else:
        print(f"'{test}' n'est pas un entier.")
        

for test in tests2:
    match = re.search(pattern, test)
    if match:
        # Extraire les groupes capturés
        number_23 = match.group(1)
        year_2024 = match.group(2)
        print(f'Nombre : {number_23}, Année : {year_2024}')
        

text = "He had prudently disguised himself but was quickly captured by the police."
pattern = r'\b\w+ly\b'

matches = re.findall(pattern, text)
print(matches)


pattern = r'^[A-Z]{2}-\d{3}-[A-Z]{2}$'

plate = input("Enter the license plate : ")

if re.fullmatch(pattern, plate): #match verify juste the start of the character
    print("the {} plate is correct".format(plate))
else:
    print("the {} plate isn't good".format(plate))
    
pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'

# Lire l'entrée de l'utilisateur
ip_address = input("Enter an IPv4 address: ")

if (re.fullmatch(pattern, ip_address)):
    print("The IPV4 {} is correct".format(ip_address))
else:
    print("The IPV4 {} isn't correct".format(ip_address))

pattern_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
pattern_password = r'^[a-zA-Z0-9._%+-]{12}$'

# Lire l'entrée de l'utilisateur
email = input("Enter your email address: ")
password = input("Enter your password: ")

# Vérifier l'adresse email
if re.fullmatch(pattern_email, email):
    print("Email is good")
    
    # Vérifier le mot de passe seulement si l'email est valide
    if re.fullmatch(pattern_password, password):
        print("Password is good")
        print("You are connected")
    else:
        print("Invalid password")
else:
    print("Invalid email address")