# Let's find out what's going on there
file = open("/home/jordan/Bureau/becode/my-repo/Python/advanced/data.txt", "r")
print (file.read())
file.close()


with open("/home/jordan/Bureau/becode/my-repo/Python/advanced/data.txt", "r") as fichier:
    print (fichier.read()) #methode without closing file 
    
file = open("/home/jordan/Bureau/becode/my-repo/Python/advanced/write.txt", "a")
writeText = input('write something : \n')
file.write("{}".format(writeText))
print()
file.close()

with open("/home/jordan/Bureau/becode/my-repo/Python/advanced/write.txt") as fichier:
    print (fichier.read())


#Récupération de tout le data "Data" pour transformer ton son contenu lowercase en uppercase 

data_file_path = "/home/jordan/Bureau/becode/my-repo/Python/advanced/write.txt"
writing_file_path = 'write.txt'

# Step 1: Read the content of the data file
with open(data_file_path, 'r') as data_file:
    content = data_file.read()

# Step 2: Capitalize all the words
capitalized_content = content.upper()

# Step 3: Append the capitalized content to the writing file
with open(writing_file_path, 'a') as writing_file:
    writing_file.write(capitalized_content)

print("Content has been capitalized and appended successfully.")