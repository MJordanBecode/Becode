# Little program to calculate

# Initialisation des variables
number1 = None
number2 = None
result = None

print("Hello! This program is used for calculation :)")

# Récupérer les deux nombres de l'utilisateur
input_string = input("Please choose two numbers, separated by a comma (e.g., 5, 10): ")

try:
    # Séparer les deux nombres
    number1, number2 = input_string.split(',')
    
    # Convertir les nombres en entiers
    number1 = int(number1.strip())
    number2 = int(number2.strip())
    
    print("You entered:")
    print("First number:", number1)
    print("Second number:", number2)
    
    # Afficher les options d'opération
    print("""Please choose your operator:
          1. +
          2. -
          3. *
          4. /
          """)
    
    # Récupérer l'opérateur choisi
    operator_input = input("Choose your operator (1 = +, 2 = -, 3 = *, 4 = /) :")

    # Effectuer le calcul en fonction de l'opérateur
    if operator_input == '1':
        result = number1 + number2
        print("Result of the addition = ", result)
    elif operator_input == '2':
        result = number1 - number2
        print("Result of the subtraction = ", result)
    elif operator_input == '3':
        result = number1 * number2
        print("Result of the multiplication = ", result)
    elif operator_input == '4':
        if number2 != 0:
            result = number1 / number2
            print("Result of the division = ", result)
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Error: Choose a valid operator.")
except ValueError:
    print("Invalid input. Please enter two numbers separated by a comma.")
