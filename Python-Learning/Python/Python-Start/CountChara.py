
input_first_string = input('say something : ')
input_second_string = input('say something again : ')

print('Your first string  = {} character.s'.format(len(input_first_string)))
print('Your second string  = {} character.s'.format(len(input_second_string)))

if((len(input_first_string) < len(input_second_string))):
    print('the bigger is the second string : ', input_second_string)
elif((len(input_first_string) < len(input_second_string))):
    print('the bigger is the first string : ', input_first_string)
else :
    print('same number of character.s')