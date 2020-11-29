import Draw
import random as r

class Star:
    def __init__(self, x, y, size, speed):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed

class Starfield:
    def __init__(self, drawCtx, density): # density is the total amount of on screen units
        self.drawCtx = drawCtx
        self.stars = [Star(r.randint(0, 800), r.randint(0, 600), r.randint(1, 3), r.randint(1,10)) for star in range(density)]

    def draw(self):
        self.drawStars()

    def update(self, dt):
        self.updateStars(dt)

    def updateStars(self, dt):
        for star in self.stars:
            if star.y > 600: 
                star.y = -5
            else:
                star.y += (star.speed * dt)
            
    def drawStars(self):
        for star in self.stars:
            Draw.drawRect(self.drawCtx, (255, 255, 255), (star.x, star.y, star.size, star.size))



