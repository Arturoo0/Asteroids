import Draw
import math
from GameState import gameState
import Entities
from Asteroid import Asteroid 

class Projectile:
    drawCtx = None
    size = 5
    speed = 50

    def __init__(self, drawCtx):
        self.drawCtx = drawCtx

    def shoot(self, x, y, angle):
        Entities.projectiles.append([x, y, angle])

    def draw(self):
        for projectile in Entities.projectiles:
            Draw.drawRect(self.drawCtx, (255,255,255), (projectile[0], projectile[1], self.size, self.size))

    def update(self, dt):
        self.updateProjectiles(dt)
        self.checkCollisions()

    def updateProjectiles(self, dt):
        for projectile in Entities.projectiles:
            projectile[0] += (self.speed * dt) * math.cos(projectile[2])
            projectile[1] += (self.speed * dt) * math.sin(projectile[2])

    def checkCollisions(self):
        for asteroid in Entities.asteroids:
            for projectile in Entities.projectiles:
                xCheck = False
                yCheck = False
                if projectile[0] >= asteroid[0]:
                    if projectile[0] <= asteroid[0] + Asteroid.size: 
                        xCheck = True
                elif asteroid[0] >= projectile[0]:
                    if asteroid[0] <= projectile[0] + self.size:
                        xCheck = True
                if projectile[1] >= asteroid[1]:
                    if projectile[1] <= asteroid[1] + Asteroid.size: 
                        yCheck = True
                elif asteroid[1] >= projectile[1]:
                    if asteroid[1] <= projectile[1] + self.size:
                        yCheck = True
                
                if xCheck and yCheck:
                    gameState['score'] += 1
                    asteroid[-1] = 2