import os.path
import re

#help(os.path)

"""path=os.path.abspath('')
print('Voici moooooooon path : ',path)"""

"""print(os.path.basename(path))"""


#Add directory 
"""rep_text=os.path.join(path, "text")
print(rep_text)"""

# Items are returned to a list and include folders and hidden files.
print(os.listdir("../"))

#How to display all the elements of a folder as well as its child folders?
path = os.path.abspath('../')
folder_path = path
data_file_path = "/home/jordan/Bureau/becode/my-repo/Python/advanced/final.txt"
final_file_path = '/home/jordan/Bureau/becode/my-repo/Python/advanced/final.txt' 

# Parcourir le répertoire et ses sous-répertoires
with open(final_file_path, 'a') as final_file:
    # Parcourir le répertoire et ses sous-répertoires
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            # Vérifier si le fichier a l'extension .txt
            if filename.endswith('.txt'):
                # Construire le chemin complet du fichier source
                data_file_path = os.path.join(root, filename)
                
                # Lire le contenu du fichier source
                with open(data_file_path, 'r') as data_file:
                    content = data_file.read()
                    print(content)
                
                # Écrire le contenu dans le fichier final
                final_file.write(f"--- Contenu du fichier : {filename} ---\n")
                final_file.write(content)
                final_file.write("\n\n")  # Ajouter une séparation entre les contenus des fichiers