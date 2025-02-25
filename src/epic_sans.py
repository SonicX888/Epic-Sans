import pygame
import pygame_menu
import math

class Epic_sans(pygame.sprite.Sprite):
    # Initialisation du joueur
    # @param x - Coordonnées X du joueur ; en fonction du coin supérieur gauche.
    # @param y - Coordonnées Y du joueur ; en fonction du coin supérieur gauche.
    def __init__(self, x, y):
        super().__init__()

        self.animation = 0
        self.value = 0

        self.image = pygame.image.load("assets/images/spritesheets/Phase_2_result.png")  # On commence à la première frame
        # width, height = self.image.get_size()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        # Image de départ
        # self.rect = pygame.Rect(center(width, height)[0], center(width, height)[1], width, height)

    def update(self):

        self.animation += 1
        #self.value = (math.sin(self.animation * 1.5) * 1.5) + (math.sin(self.animation * 1.5) * 1.5)

    # Fonction récurrente de dessin
    def draw(self, screen):
        screen.blit(self.image, self.rect)

