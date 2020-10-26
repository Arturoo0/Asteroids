import pygame
import Draw as draw
import math
class Player:
    def __init__(self, displayCtx, velocity):
        self.velocity = velocity
        self.displayCtx = displayCtx
        self.polygonRepresentation = [[30, 30], [45, 75], [15, 75]]
        self.speed = 30
        self.keysHeld = {
            'a' : False, 
            'w' : False,
            'd' : False,
            's' : False 
        }
    
    def draw(self):
        draw.drawPolygon(self.displayCtx, (255, 255, 255), self.polygonRepresentation, fillType=1)

    def update(self, dt):
        print(self.getPlayerAngle())
        self.computeMovement(dt)
    
    def trackKeyPresses(self, event):
        if event.type == pygame.KEYDOWN:
            self.keysHeld[chr(event.key)] = True
        if event.type == pygame.KEYUP:
            self.keysHeld[chr(event.key)] = False
    
    def computeMovement(self, dt):
        for k,v in self.keysHeld.items():
            if v:
                if k == 'a': self.rotate(self.computeCentroid(), -1.5 * dt)
                if k == 'w': self.shiftPlayerForward(self.getPlayerAngle(), dt)
                if k == 'd': self.rotate(self.computeCentroid(), 1.5 * dt)
    
    def computeCentroid(self):
        centroidX = 0
        centroidY = 0
        for pair in self.polygonRepresentation:
            centroidX += pair[0]
            centroidY += pair[1]
        return (centroidX/3, centroidY/3)
    
    def rotate(self, centroid, angle) :
        ox, oy = centroid
        for point in self.polygonRepresentation:
            dx = point[0] - ox
            dy = point[1] - oy

            rx = dx * math.cos(angle) - dy * math.sin(angle)
            ry = dx * math.sin(angle) + dy * math.cos(angle)

            point[0] = rx + ox
            point[1] = ry + oy
        
    def getPlayerAngle(self):
        centX, centY = self.computeCentroid()
        dx = self.polygonRepresentation[0][0] - centX
        dy = self.polygonRepresentation[0][1] - centY
        return (math.atan2(dy, dx))
    
    def shiftPlayerForward(self, angle, dt):
        for point in self.polygonRepresentation:
            point[0] += (self.speed * dt) * math.cos(angle)
            point[1] += (self.speed * dt) * math.sin(angle)


    
    
    


 