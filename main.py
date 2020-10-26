import pygame
import Player
import Asteroid

def main():
    pygame.init()

    clock = pygame.time.Clock()
    display = pygame.display.set_mode((800, 600))
    mainPlayer = Player.Player(display, 10)
    asteroid = Asteroid.Asteroid(display)
    
    running = True

    while running:
        dt = 1 / float(clock.tick(60))
        display.fill((0, 0, 0))
        for event in pygame.event.get():
            mainPlayer.trackKeyPresses(event)
            if event.type == pygame.QUIT:
                running = False
        
        mainPlayer.update(dt)
        mainPlayer.draw()

        asteroid.update(dt)
        asteroid.draw()
        
        mainPlayer.draw()
        pygame.display.update()

if __name__== "__main__":
    main()