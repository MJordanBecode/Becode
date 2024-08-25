# Ouvrir le fichier en mode lecture
with open("/home/jordan/Bureau/becode/my-repo/Python/advanced/testmail.txt", 'r') as list_mail:
    # Lire toutes les lignes du fichier
    emails = list_mail.readlines()
    
    # Supprimer les caractères de nouvelle ligne et afficher les adresses e-mail
    emails = [email.strip() for email in emails]
    
    # Afficher les adresses e-mail
    for email in emails:
        print(email)

list_mail = open("/home/jordan/Bureau/becode/my-repo/Python/advanced/testmail.txt")