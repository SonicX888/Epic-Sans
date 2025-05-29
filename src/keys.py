# --- Class: Keys ---
# Purpose: Captures and stores the current keyboard input state for game controls
import pygame

class Keys:
    def __init__(self):
      # Poll all current key states
      self.keys = pygame.key.get_pressed()

      # Action keys
      self.z = self.keys[pygame.K_z]      # Confirm / attack / interact
      self.x = self.keys[pygame.K_x]      # Cancel / back
      self.e = self.keys[pygame.K_e] # Enable debug mode
      self.d = self.keys[pygame.K_d] # Disable debug mode

      # Movement keys for arrow controls
      self.up = self.keys[pygame.K_UP]
      self.down = self.keys[pygame.K_DOWN]
      self.left = self.keys[pygame.K_LEFT]
      self.right = self.keys[pygame.K_RIGHT]
