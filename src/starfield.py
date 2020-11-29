import Draw
import random as r

class Star:
    def __init__(x, y, size):

class Starfield:

    def __init__(self, drawCtx, density): # density is the total amount of on screen units
        self.drawCtx = drawCtx
        self.stars = [(r.randint(0, 800), r.randint(-20, 0), r.randint(1, 3)) for star in range(density)]

    def draw(self):
        self.drawStars()

    def update(self, dt):
        self.updateStars(dt)

    def updateStars(self, dt):
        for pos in range(len(self.stars)):
            x, y, vel = self.stars[pos]
            if y > 600: 
                self.stars[pos] = (x, -10, vel)
            else:
                self.stars[pos] = (x, y + (vel * dt), vel)
            
    def drawStars(self):
        for star in self.stars:
            size = r.randint(1,3)
            Draw.drawRect(self.drawCtx, (255, 255, 255), (star[0], star[1], size, size))



