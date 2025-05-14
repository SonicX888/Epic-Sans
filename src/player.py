import pygame
from keys import Keys

class Player(pygame.sprite.Sprite):
    def __init__(self):

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
        self.x_soul = (1000 - self.width_soul) // 2
        self.y_soul = 400
        self.rect_soul = pygame.Rect(self.x_soul, self.y_soul, self.width_soul, self.height_soul)

    def update(self, box, beam_rects=[]):

        keys = Keys()

        if keys.up and self.rect_soul.colliderect(box):
            self.rect_soul.centery -= self.speed
            if not self.rect_soul.colliderect(box):
                self.rect_soul.centery += self.speed
        if keys.down and self.rect_soul.colliderect(box):
            self.rect_soul.centery += self.speed
            if not self.rect_soul.colliderect(box):
                self.rect_soul.centery -= self.speed
        if keys.left and self.rect_soul.colliderect(box):
            self.rect_soul.centerx -= self.speed
            if not self.rect_soul.colliderect(box):
                self.rect_soul.centerx += self.speed
        if keys.right and self.rect_soul.colliderect(box):
            self.rect_soul.centerx += self.speed
            if not self.rect_soul.colliderect(box):
                self.rect_soul.centerx -= self.speed
        
        '''if keys.up:
            self.rect_soul.centery -= self.speed
        if keys.down:
            self.rect_soul.centery += self.speed
        if keys.left:
            self.rect_soul.centerx -= self.speed
        if keys.right:
            self.rect_soul.centerx += self.speed'''

        self.collision = False
        for beam_rect in beam_rects:
            if self.rect_soul.colliderect(beam_rect):
                self.collision = True
                break


    def draw(self, surface):
        surface.blit(self.soul, self.rect_soul)