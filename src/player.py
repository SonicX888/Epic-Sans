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
        self.broken_sound = pygame.mixer.Sound("assets/sounds/sound_effects/broken.wav")
        self.soul = self.souls[0]
        self.broken = self.souls[3]
        self.width_soul, self.height_soul = self.soul.get_size()
        self.x_soul = (1000 - self.width_soul) // 2
        self.y_soul = 400
        self.rect_soul = pygame.Rect(self.x_soul, self.y_soul, self.width_soul, self.height_soul)
        self.gameover = False

    def update(self, box, hp, beam_rects=[], beam_alphas=[], bonewall_rects=[]):
        if hp > 0:
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

            # Collision avec les beams
            self.collision = False
            for beam_rect in beam_rects:
                for beam_alpha in beam_alphas:
                    if beam_alpha != 0:
                        if self.rect_soul.colliderect(beam_rect.inflate(-75, -75)):
                            self.collision = True
                            break

            # Collision avec les bonewalls
            for bonewall_rect in bonewall_rects:
                if self.rect_soul.colliderect(bonewall_rect):
                    self.collision = True
                    break

    def draw(self, surface, hp):
        if hp <= 0 and self.gameover == False:
            pygame.mixer.Channel(0).stop()
            self.broken_sound.play()
            self.gameover = True

        if hp > 0:
            surface.blit(self.soul, self.rect_soul)
        else:
            surface.blit(self.broken, self.rect_soul)
        