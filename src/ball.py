import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, speed):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(pygame.image.load("assets/images/attacks/others/ball.png"), (50, 50))
            self.rect = self.image.get_rect(center = (x, y))
            self.pos = (x, y)
            self.direction = direction
            self.speed = speed

    def calculate_new_xy(self, old_xy, speed, angle_in_degrees):
        move_vec = pygame.math.Vector2()
        move_vec.from_polar((speed, angle_in_degrees))
        return old_xy + move_vec

    def update(self, surface):
            self.pos = self.calculate_new_xy(self.pos, self.speed, -self.direction)
            self.rect.center = round(self.pos[0]), round(self.pos[1])
            if not surface.get_rect().colliderect(self.rect):
                self.kill()
    def draw(self, surface):
         surface.blit(self.image, self.rect)