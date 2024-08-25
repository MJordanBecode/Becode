from lxml import etree  #besoin d'installer lxml avant d'utiliser des composants qui se relie à lui : pip install lxml 

# Analyser une chaîne XML
xml_string = '''<root><child>content</child></root>'''
root_from_string = etree.fromstring(xml_string)

# Afficher le contenu de la chaîne XML
print("Contenu analysé depuis la chaîne XML :")
print(etree.tostring(root_from_string, pretty_print=True).decode('utf-8'))

# Analyser un fichier XML
file_path = '/home/jordan/Bureau/becode/my-repo/Python/advanced/lxml&tree/xml/test.xml'  # Assurez-vous que l'extension est correcte

try:
    tree = etree.parse(file_path) #va rechercher l'endroit ou se retrouve le fichier grâce au path donné et il va le lire 
    root_from_file = tree.getroot()

    # Afficher le contenu du fichier XML
    print("\nContenu analysé depuis le fichier XML :")
    print(etree.tostring(root_from_file, pretty_print=True).decode('utf-8'))

except (etree.XMLSyntaxError, IOError) as e:
    print(f"Erreur lors de l'analyse du fichier XML : {e}")


#We can use param in the request to take exemple just job "Veterinaire"

tree = etree.parse("../data/data.xml")
# Quel joli petit dictionnaire
for user in tree.xpath("/users/user[metier='Veterinaire']/nom"):
    print(user.text)
    
# You can display the attributes of the tags that store this information
tree = etree.parse("../data/data.xml")
for user in tree.xpath("/users/user"):
    print(user.get("data-id"))