import sys
sys.path.append('./src')
import pygame
import Player
import Asteroids
import Projectile
import Scoreboard
import GameState
import Menu

def main():
    pygame.init()
    clock = pygame.time.Clock()
    display = pygame.display.set_mode((800, 600))

    mainPlayer = Player.Player(display, 10)
    asteroid = Asteroids.Asteroids(display)
    projectiles = Projectile.Projectile(display)
    scoreboard = Scoreboard.Scoreboard(display)
    menu = Menu.Menu(display)
    
    running = True

    while running:
        dt = 1 / float(clock.tick(60))
        display.fill((0, 0, 0))
        for event in pygame.event.get():
            mainPlayer.trackKeyPresses(event)
            menu.trackKeyPresses(event)
            if event.type == pygame.QUIT:
                running = False

        if not GameState.gameState['inMenu']:
            mainPlayer.update(dt)
            mainPlayer.draw()

            asteroid.update(dt)
            asteroid.draw()

            projectiles.update(dt)
            projectiles.draw()

            scoreboard.draw()
        else:
            menu.draw()
            menu.update(dt)
            

        pygame.display.update()

if __name__== "__main__":
    main()