#List and Dictionnary
translate_list = ('Table', 'Chair', 'Moon', 'Love', 'Romantic')

print(translate_list)
translate_list = {}
translate_list['Table'] = 'Table'
translate_list['Chair'] = 'Chaise'
translate_list['Moon'] = 'Lune'
translate_list['Love'] = 'Amour'
translate_list['Romantic'] = 'Romantique'

translate_list['I am the master of the world'] = "I am the master of the world".split()

print(translate_list)

universalNumber =  "The_universal_number_is_42" 

#replace 
replace_universalNumber = universalNumber.replace("_", "")
print(replace_universalNumber)

heroes = {"Superman" : "Clark kent", "Batman" : "Bruce Wayne", "Spiderman" : "Tony Parker"}

# Print each value
for value in heroes.values():
    print(value)
    
    # Print each ky-ey
for value in heroes.keys():
    print(value)
    
    heroes['Spiderman'] = 'Peter Parker'
print(heroes)

# Dictionnaire des produits avec leurs prix
products = {
    'Laser sword': 229.0,
    'Mitendo DX': 127.30,
    'Linux cushion': 74.50,
    'Goldorak briefs': 29.90,
    'Nextpresso station': 184.60
}

#delete something in a table use Del[return an Error] or Pop[Pop return an error if the key don't exist and we can define it]
del products['Laser sword']
remove_value = products.pop('Goldorak briefs','Key not found')
total = sum(products.values())
print(total)


