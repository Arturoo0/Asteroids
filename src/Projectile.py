import Draw
import math
from GameState import gameState
import Entities
from Asteroids import Asteroids
import random as r

class Projectile:
    drawCtx = None
    size = 5
    speed = 50

    def __init__(self, drawCtx):
        self.drawCtx = drawCtx
        self.asteroidObj = Asteroids(drawCtx)

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
                xCheck = True
                yCheck = True
            
                if (projectile[0] >= asteroid[0] + asteroid[-2]) or (asteroid[0] >= projectile[0] + self.size):
                    xCheck = False 
                if projectile[1] >= asteroid[1] + asteroid[-2] or asteroid[1] >= projectile[1] + self.size:
                    xCheck = False 
            
                if xCheck and yCheck:
                    gameState['score'] += 1
                    asteroid[-1] = 2
                    if asteroid[-2] > self.asteroidObj.sizeLimit: 
                        for i in range(2):
                            newXComponent = asteroid[2] * r.uniform(.5,1)
                            newYComponent = asteroid[3] * r.uniform(.5, 1)
                            self.asteroidObj.addAsteroid(asteroid[0] + newXComponent, asteroid[1] + newYComponent, newXComponent, newYComponent, asteroid[-2]//2)