import pygame
import sys

# Initialiser Pygame
pygame.init()

# Créer la fenêtre de jeu
fenetre = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Jeu Simple')

# Charger l'image du personnage
perso = pygame.image.load('/home/jordan/Bureau/becode/my-repo/Python/game/perso.jpg').convert()

# Obtenir la taille de l'image et de la fenêtre
perso_width, perso_height = perso.get_size()
fenetre_width, fenetre_height = fenetre.get_size()

# Calculer les dimensions de l'image en gardant le rapport d'aspect
if (fenetre_width / perso_width) < (fenetre_height / perso_height):
    new_width = fenetre_width
    new_height = int((perso_height * fenetre_width) / perso_width)
else:
    new_width = int((perso_width * fenetre_height) / perso_height)
    new_height = fenetre_height

# Redimensionner l'image du personnage
perso = pygame.transform.scale(perso, (new_width, new_height))

# Initialiser les coordonnées du personnage
x, y = (fenetre_width - new_width) // 2, (fenetre_height - new_height) // 2
vitesse = 5
clock = pygame.time.Clock()

while True:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Gestion des touches
    touches = pygame.key.get_pressed()
    if touches[pygame.K_LEFT]:
        x -= vitesse
    if touches[pygame.K_RIGHT]:
        x += vitesse
    if touches[pygame.K_UP]:
        y -= vitesse
    if touches[pygame.K_DOWN]:
        y += vitesse

    # S'assurer que le personnage reste dans les limites de la fenêtre
    x = max(0, min(x, fenetre_width - new_width))
    y = max(0, min(y, fenetre_height - new_height))

    fenetre.fill((255, 255, 255))  # Remplit l'écran avec du blanc
    fenetre.blit(perso, (x, y))  # Affiche l'image du personnage

    pygame.display.flip()  # Met à jour l'affichage
    clock.tick(60)  # Limite la boucle à 60 FPS
