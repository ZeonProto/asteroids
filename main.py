#   imports the pygame library
import pygame
#   imports everything from the constants.py file
from constants import *
#   imports the 'Player' class from player.py
from player import Player


def main():
    #   initializes pygame
    pygame.init()
    #   sets the screen size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #   creates a clock to check the framerate
    clock = pygame.time.Clock()
    #   creates the player object and gives it the parameters for the class
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    #   delta time
    dt = 0

    #   infinite loop to make the game run
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #   updates the player object based on input
        player.update(dt)
        
        #   gives a background to the screen
        screen.fill("black")
        #   draws the player object on screen
        player.draw(screen)
        #   function to refresh the display
        pygame.display.flip()

        #   caps the fps at 60 and adds it to the delta time
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
    