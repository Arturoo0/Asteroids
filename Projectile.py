import Draw
import math
class Projectile:
    projectileEntities = []
    drawCtx = None
    size = 5
    speed = 50

    def __init__(self, drawCtx):
        self.drawCtx = drawCtx

    def shoot(self, x, y, angle):
        self.projectileEntities.append([x, y, angle])

    def draw(self):
        for projectile in self.projectileEntities:
            Draw.drawRect(self.drawCtx, (255,255,255), (projectile[0], projectile[1], self.size, self.size))

    def update(self, dt):
        for projectile in self.projectileEntities:
            projectile[0] += (self.speed * dt) * math.cos(projectile[2])
            projectile[1] += (self.speed * dt) * math.sin(projectile[2])

