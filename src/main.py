import pygame
from game import Game

def main():
    # Appel de la classe jeu (game.py)
    # Démmarage du jeu
    pygame.init()
    icon = pygame.image.load("assets/images/icon.png")
    pygame.display.set_caption('Epic!Sans Fight')
    pygame.display.set_icon(icon)
    game = Game()
    game.run()
    # Fermeture du jeu
    pygame.quit()

if __name__ == "__main__":
    main()