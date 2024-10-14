#   imports the pygame library
import pygame
#   imports everything from the constants.py file
from constants import *
#   imports classes for other files
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    #   initializes pygame
    pygame.init()
    #   sets the screen size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #   creates a clock to check the framerate
    clock = pygame.time.Clock()
    
    #   creates a groups for objects to inhabit
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #   Assigns the various objects to their groups
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    #   creates the 'asteroid_field' object
    asteroid_field = AsteroidField()

    #   add the player to the 'updatable' group and 'drawable' group 
    Player.containers = (updatable, drawable)

    #   creates the player object and gives it the parameters for the class
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #   delta time
    dt = 0

    #   infinite loop to make the game run
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #   updates the updatable objects based on input
        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player) == True:
                print("Game Over!")
                return pygame.QUIT
            
            for shot in shots:
                if shot.collision(asteroid) == True:
                    shot.kill(), asteroid.kill()
        
        #   gives a background to the screen
        screen.fill("black")

        #   draws the drawable objects on screen
        for obj in drawable:
            obj.draw(screen)

        #   function to refresh the display
        pygame.display.flip()

        #   caps the fps at 60 and adds it to the delta time
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
    