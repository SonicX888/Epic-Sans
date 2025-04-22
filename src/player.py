import pygame
from decorations import Decorations
from keys import Keys
from hp import HP

class Player(pygame.sprite.Sprite):
    def __init__(self):

        self.decorations = Decorations()
        self.hp = HP()

        self.speed = 5
        self.size = (30, 30)
        self.collision = False

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

        keys = Keys()

        if keys.up and self.rect_soul.colliderect(self.decorations.hitbox):
            self.rect_soul.centery -= self.speed
            if not self.rect_soul.colliderect(self.decorations.hitbox):
                self.rect_soul.centery += self.speed
        if keys.down and self.rect_soul.colliderect(self.decorations.hitbox):
            self.rect_soul.centery += self.speed
            if not self.rect_soul.colliderect(self.decorations.hitbox):
                self.rect_soul.centery -= self.speed
        if keys.left and self.rect_soul.colliderect(self.decorations.hitbox):
            self.rect_soul.centerx -= self.speed
            if not self.rect_soul.colliderect(self.decorations.hitbox):
                self.rect_soul.centerx += self.speed
        if keys.right and self.rect_soul.colliderect(self.decorations.hitbox):
            self.rect_soul.centerx += self.speed
            if not self.rect_soul.colliderect(self.decorations.hitbox):
                self.rect_soul.centerx -= self.speed

        if not self.rect_soul.colliderect(self.decorations.hitbox):
            self.collision = True
        else:
            self.collision = False

    def draw(self, surface):
        surface.blit(self.soul, self.rect_soul)