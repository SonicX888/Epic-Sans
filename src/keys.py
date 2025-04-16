import pygame

class Keys:
  
  def __init__(self):
    # Touches du clavier

    self.keys = pygame.key.get_pressed()
    self.z = self.keys[pygame.K_z]
    self.x = self.keys[pygame.K_x]
    self.esc = self.keys[pygame.K_ESCAPE]

    self.up = self.keys[pygame.K_UP]
    self.down = self.keys[pygame.K_DOWN]
    self.left = self.keys[pygame.K_LEFT]
    self.right = self.keys[pygame.K_RIGHT]