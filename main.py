#   imports the pygame library
import pygame
#   imports everything from the constants.py file
from constants import *
from player import Player


def main():
    #   initializes pygame
    pygame.init()
    #   sets the screen size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #   creates a clock to check the framerate
    clock = pygame.time.Clock()
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    #   delta time
    dt = 0

    #   infinite loop to make the game run
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #   gives a background to the screen
        screen.fill("black")
        
        player.draw(screen)
        #   function to refresh the display
        pygame.display.flip()

        #   caps the fps at 60 and adds it to the delta time
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
    