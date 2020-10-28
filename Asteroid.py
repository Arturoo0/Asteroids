import random
import Draw as draw
import copy
import Entities

class Asteroid:
    callInterval = 0
    size = 30
    xSpeed = 45
    ySpeed = 45

    def __init__(self, displayCtx):
        self.displayCtx = displayCtx

    def update(self, dt):
        self.callInterval += 1
        if self.callInterval % 100 == 0:
            self.generateAsteroid()
        self.pruneEntities(dt)
    
    def draw(self):
        for asteroid in Entities.asteroids:
            draw.drawRect(self.displayCtx, (255, 255, 255), (asteroid[0], asteroid[1], self.size, self.size), fillType=1)
 
    def pruneEntities(self, dt):
        newEntities = []
        for asteroid in Entities.asteroids:
            if asteroid[-1] == 0 and self.inScreen(asteroid):
                asteroid[-1] += 1
            if asteroid[-1] == 1 and not self.inScreen(asteroid) or asteroid[-1] == 2:
                asteroid[-1] = 2
                continue
            asteroid[0] += asteroid[2] * dt
            asteroid[1] += asteroid[3] * dt
            newEntities.append(asteroid)
        Entities.asteroids = copy.deepcopy(newEntities)

    def inScreen(self, asteroid):
        x, y = asteroid[0], asteroid[1]
        return (x >= 0 and x <= 800) and (y >= 0 and y <= 600)
 
    def generateAsteroid(self):
        xFlip = random.randint(0, 1)
        yFlip = random.randint(0, 1)
        xComponent, yComponent = 0, 0

        if xFlip == 0:
            y = random.randint(-20, 620)
            self.addAsteroid(-10, y, self.xSpeed, random.randint(-5, 5))
        else: 
            y = random.randint(-20, 620)
            self.addAsteroid(810, y, -self.xSpeed, random.randint(-5, 5)) 

        if yFlip == 0:
            x = random.randint(-20, 820)
            self.addAsteroid(x, -10, random.randint(-5, 5), self.ySpeed)
        else: 
            x = random.randint(-20, 820)
            self.addAsteroid(x, 620, random.randint(-5,5), -self.ySpeed)

    def addAsteroid(self, x, y, xComponent, yComponent):
        Entities.asteroids.append([x, y, xComponent, yComponent, 0])
