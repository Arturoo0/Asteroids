import pygame
import Draw as draw
import math
import Projectile

class Player:
    def __init__(self, displayCtx, velocity):
        self.projectile = Projectile.Projectile(displayCtx)
        self.xVelocity = 0
        self.yVelocity = 0
        self.currentPlayerSpeed = 0
        self.displayCtx = displayCtx
        self.polygonRepresentation = [[30, 30], [40, 60], [20, 60]]
        self.speed = 40
        self.deceleration = .99
        self.acceleration = 1.05
        self.rotationSpeed = 1.5
        self.keysHeld = {
            'a' : False, 
            'w' : False,
            'd' : False,
            's' : False 
        }
    
    def draw(self):
        draw.drawPolygon(self.displayCtx, (255, 255, 255), self.polygonRepresentation, fillType=1)

    def update(self, dt):
        print(self.currentPlayerSpeed)
        self.computeMovement(dt)
        self.applyInertia(dt)
    
    def trackKeyPresses(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == 32:
                x = self.polygonRepresentation[0][0]
                y = self.polygonRepresentation[0][1]
                self.projectile.shoot(x, y, self.getPlayerAngle())
            else:
                self.keysHeld[chr(event.key)] = True
        if event.type == pygame.KEYUP:
            self.keysHeld[chr(event.key)] = False

    def computeMovement(self, dt):
        for k,v in self.keysHeld.items():
            if v:
                if k == 'a': self.rotate(self.computeCentroid(), -self.rotationSpeed * dt)
                if k == 'w': self.shiftPlayerForward(self.getPlayerAngle(), dt)
                if k == 'd': self.rotate(self.computeCentroid(), self.rotationSpeed * dt)

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
        dx = (self.speed * dt) * math.cos(angle)
        dy = (self.speed * dt) * math.sin(angle)
        if self.currentPlayerSpeed == 0: self.currentPlayerSpeed = 0.5
        if abs(self.currentPlayerSpeed < self.speed): self.currentPlayerSpeed *= self.acceleration
        for point in self.polygonRepresentation:
            point[0] += dx 
            point[1] += dy
            self.xVelocity = dx * 20
            self.yVelocity = dy * 20
    
    def applyInertia(self, dt):
        if not self.keysHeld['w'] and (abs(self.xVelocity > 0) or abs(self.yVelocity) > 0):
            for point in self.polygonRepresentation:
                point[0] += self.xVelocity * dt
                point[1] += self.yVelocity * dt
            
            if abs(self.xVelocity) < 1: self.xVelocity = 0 
            if abs(self.yVelocity) < 1: self.yVelocity = 0 

            self.xVelocity *= self.deceleration
            self.yVelocity *= self.deceleration
            self.currentPlayerSpeed *= self.deceleration

    
    
    


 