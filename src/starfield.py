import Draw
import random as r

class Starfield:

    def __init__(self, drawCtx, density): # density is the total amount of on screen units
        self.drawCtx = drawCtx
        self.stars = [(r.randint(0, 800), r.randint(0, 600)) for star in range(density)]

    def draw(self):
        self.drawStars()

    def update(self):
        self.renderStars()

    # def updateStars(self):
        

    def drawStars(self):
        for star in stars:
            size = r.randint(1,3)
            Draw.drawRect(self.drawCtx, (255, 255, 255), (star[0], star[1], size, size))



