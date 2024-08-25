print('Welcome to the game Bigger or Smoller ? Choose your numbers ! ')
input_number1 = int(input('Choose the number 1 :'))
input_number2 = int(input('Choose the number 2 :'))

# Vérifier si les nombres sont négatifs
if input_number1 < 0 or input_number2 < 0:
    print('Error: Invalid number, please choose a number >= 0')
# Comparer les deux nombres
elif input_number1 < input_number2:
    print('The bigger number is:', input_number2)
elif input_number1 > input_number2:
    print('The bigger number is:', input_number1)
else:
    print('Both numbers are equal.')