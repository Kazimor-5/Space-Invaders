import pygame
import random
import math

from pygame import mixer

# Initialisation Pygame
pygame.init()

# Creation de la fenêtre
screen = pygame.display.set_mode((800, 600))  # Height = Y, width = X

# Background
background = pygame.image.load('./background.jpg')

# Background Sound
mixer.music.load('./background.wav')
mixer.music.play(-1)

# Titre et icône
# Titre
pygame.display.set_caption("Space Invaders")

# Icône
icon = pygame.image.load('./ufo.png')
pygame.display.set_icon(icon)

# Joueur
player_img = pygame.image.load('./spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

# Ennemis
enemy_img = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemy_img.append(pygame.image.load('./alien.png'))
    enemyX.append(random.randint(0, 735))  # valeur random dans le X
    enemyY.append(random.randint(50, 150))  # valeur random dans le Y
    enemyX_change.append(0.3)
    enemyY_change.append(40)

# Balles
bullet_img = pygame.image.load('./bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 2
bullet_state = "ready"  # ready = on ne voit pas la balle, fire = la balle est en train de bouger

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)


# Fonction joueur
def player(x, y):
    screen.blit(player_img, (x, y))


# Fonction ennemi
def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))


# Fonction balles
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))


# Fonction collisions
def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((math.pow(enemyX[i] - bulletX, 2)) + (math.pow(enemyY[i] - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False
    # distance entre 2 coordonnées = d = √((x2 − x1)² + (y2 − y1)²)


# Fonction score
def show_score(x, y):
    score = font.render('Score: ' + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


# Fonction Game Over
def game_over_text():
    game_over = over_font.render('GAME OVER', True, (255, 255, 255))
    screen.blit(game_over, (200, 250))


# Game Loop => utile pour tout les events de l'utilisateur

running = True

while running:
    # Couleur du background
    screen.fill((0, 0, 0))
    # Background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # vérifie si une touche a été pressé
        if event.type == pygame.KEYDOWN:
            # vérifie si la flèche gauche à été pressé
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5

            # vérifie si la flèche droite à été pressé
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5

            # vérifie si la touche espace à été pressé
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound('./laser.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        # vérifie si un touche à été relâché
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Mouvements du vaisseau
    playerX += playerX_change

    # Si le vaisseau touche les bords de la fenêtre
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:  # 736 = taille de la fenêtre - taille du sprite -> 64px * 64px => 800px - 64px
        playerX = 736

    # Mouvements de l'ennemi
    for i in range(num_of_enemies):
        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]

        # Si l'ennemi touche les bords de la fenêtre
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:  # 736 = taille de la fenêtre - taille du sprite -> 64px * 64px => 800px - 64px
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]

        # Collisions
        collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            collision_sound = mixer.Sound('./explosion.wav')
            collision_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Mouvements de la balle
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Apparition des sprites
    player(playerX, playerY)

    # Affichage du score
    show_score(textX, textY)
    # permet d'update chaque modification dans le jeu/la fenêtre
    pygame.display.update()
