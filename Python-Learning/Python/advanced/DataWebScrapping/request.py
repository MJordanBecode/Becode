import requests
from bs4 import BeautifulSoup

# URL du site web
url = 'https://www.becode.org/about/'

# Envoyer une requête GET au serveur
r = requests.get(url)

# Afficher l'URL demandée et le code de statut de la réponse
print("URL:", url)
print("Code de statut:", r.status_code)

# Analyser le contenu HTML avec BeautifulSoup
soup = BeautifulSoup(r.content, 'lxml')

# Afficher le contenu complet analysé de manière lisible
print("\nContenu complet analysé :")
print(soup.prettify())

# Extraire et afficher le titre de la page
print("\nTitre de la page :", soup.title.string)

# Extraire et afficher tous les liens (éléments <a>) présents dans la page
print("\nTous les liens :")
for link in soup.find_all('a'):
    print(link.get('href'))
