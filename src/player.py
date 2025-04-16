import pygame
from keys import Keys

class Player(pygame.sprite.Sprite):
    def __init__(self):

        self.keys = Keys()

        self.speed = 5
        self.direction = "right"

        self.size = (30, 30)

        self.souls = [
            pygame.transform.scale(pygame.image.load("assets/images/soul/red.png"), self.size),
            pygame.transform.scale(pygame.image.load("assets/images/soul/blue.png"), self.size),
            pygame.transform.scale(pygame.image.load("assets/images/soul/purple.png"), self.size),
            pygame.transform.scale(pygame.image.load("assets/images/soul/broken_soul.png"), self.size)
            ]
        self.soul = self.souls[0]
        self.width_soul, self.height_soul = self.soul.get_size()
        self.x_soul = 500
        self.y_soul = 375
        self.rect_soul = pygame.Rect(self.x_soul, self.y_soul, self.width_soul, self.height_soul)

    def update(self):

        self.moving = False
        
        # Dictionnaire pour gérer les déplacements en fonction des touches
        self.directions = {
            'up': (0, -self.speed),
            'down': (0, self.speed),
            'left': (-self.speed, 0),
            'right': (self.speed, 0)
        }

        # Vérification des touches et mise à jour de la position
        for direction, (dx, dy) in self.directions.items():
            if getattr(self.keys, direction): # Vérifie si la touche correspondant à la direction est pressée
                self.rect_soul.x += dx
                self.rect_soul.y += dy
                self.direction = direction
                self.moving = True
                break

    def draw(self, surface):
        surface.blit(self.soul, self.rect_soul)