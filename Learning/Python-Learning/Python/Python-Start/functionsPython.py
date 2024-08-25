def helloName(name):
    fixed_name = 'Jordan'
    return f'Hello, {fixed_name}!'

# Appelle la fonction
print(helloName('Alice'))


sumOfStudents = ([["Jean", "Alice", "Edwige", "Peter", "James"],
               ["Redouane", "Justine", "Adrien", "Nicolas", "Pierre"]])

all_students = [student for sublist in sumOfStudents for student in sublist] #sort toutes les données des deux tableaux pour les mettre dans un seul
print(len(all_students))


def isDivisible(n, x, y):
    if n % x == 0 and n % y == 0:
        print("{} is divisible by {} and {}".format(n, x, y))
    else:
        print("{} is not divisible by {} and {}".format(n, x, y))



isDivisible(4,5,6)
isDivisible(5,1,5)

def generate_acronym(full_name):
    # Séparer le nom complet en mots
    words = full_name.split()
    print(words)
    # Prendre la première lettre de chaque mot et les mettre en majuscules
    initials = [word[0].upper() for word in words]
    print(initials)
    # Joindre les initiales avec des points
    acronym = '.'.join(initials)
    return acronym

# Exemple d'utilisation
name = "Sam Harris"
print(generate_acronym(name))  # Affiche "S.H."

def positive_sum(numbers):
    # Filtrer les nombres positifs et calculer leur somme
    total = sum(num for num in numbers if num > 0)
    
    # Si la somme est zéro, imprimer un message
    if total == 0:
        print("No positive numbers in the list")
    
    return total

# Exemple d'utilisation
print(positive_sum([1, -4, 7, 12]))  # Affiche 20
print(positive_sum([-1, -4, -7, -12]))  # Affiche "No positive numbers in the list" puis 0


def sum_mix(arr):
    return sum(arr)
print(sum_mix([4,5,6,5,-19]))


def switch_case_day(case):
    if case == 1:
        return "Monday"
    elif case == 2:
        return "Tuesday"
    elif case == 3:
        return "Wednesday"
    elif case == 4:
        return "Thursday"
    elif case == 5:
        return "Friday"
    elif case == 6:
        return "Saturday"
    elif case == 7:
        return "Sunday"
    else:
        return "Default case"

input_user = input("Choose a number between 1 and 7 : ")
print(switch_case_day(float(input_user)))


def summation(num):
    total = 0
    for i in range(1, num + 1):
        total += i
    return total

# Exemple d'utilisation
print(summation(5))  # Affiche 15, car 1 + 2 + 3 + 4 + 5 = 15


def count_sheep(n):
    i = 1
    while i <= n:
        print("{} sheep ...".format(i))
        i += 1  # Incrémenter i correctement
    return "Finished counting sheep!"

# Exemple d'utilisation
input_sheep = input("choose a number : ")
print(count_sheep(float(input_sheep)))
