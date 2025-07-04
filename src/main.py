# --- Main Function ---
# Purpose: Initializes the game window and starts the main game loop
import pygame
from game import Game
from assets import Assets

def main():
    pygame.init()  # Initialize all Pygame modules

    # Set up game window with icon and title
    icon = pygame.image.load(Assets().icon)
    pygame.display.set_caption('Epic!Sans Fight')
    pygame.display.set_icon(icon)

    # Create Game instance and start the game loop
    game = Game()
    game.run()

    # Cleanup when game exits
    pygame.quit()

if __name__ == "__main__":
    main()
