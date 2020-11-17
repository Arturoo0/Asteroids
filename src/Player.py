import pygame
import Draw as draw
import math
import Projectile
import Entities
from Asteroid import Asteroid
from GameState import gameState

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
        self.acceleration = 1.09
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
        self.mirrorPlayer()
        self.detectPlayerCollision()
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
        dx = (self.currentPlayerSpeed * dt) * math.cos(angle)
        dy = (self.currentPlayerSpeed * dt) * math.sin(angle)

        self.xVelocity = dx * 20
        self.yVelocity = dy * 20

        if self.currentPlayerSpeed == 0: self.currentPlayerSpeed = 0.5
        if abs(self.currentPlayerSpeed < self.speed): self.currentPlayerSpeed *= self.acceleration
        for point in self.polygonRepresentation:
            point[0] += dx 
            point[1] += dy
    
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
    
    def detectPlayerCollision(self):
        for coord in self.polygonRepresentation:
            for asteroid in Entities.asteroids:
                xCheck = coord[0] >= asteroid[0] and coord[0] <= asteroid[0] + Asteroid.size
                yCheck = coord[1] >= asteroid[1] and coord[1] <= asteroid[1] + Asteroid.size
                if xCheck and yCheck: 
                    gameState['lives'] -= 1
                    self.polygonRepresentation = [[30, 30], [40, 60], [20, 60]]
                    return
    
    def mirrorPlayer(self):
        mirrorX = True
        mirrorY = True
        for coord in self.polygonRepresentation:
            if coord[0] > 0 and coord[0] < 800: mirrorX = False
            if coord[1] > 0 and coord[1] < 600: mirrorY = False
        if mirrorX:
            for coord in self.polygonRepresentation:
                coord[0] = abs(800 - coord[0])
        if mirrorY:
            for coord in self.polygonRepresentation:
                coord[1] = abs(600 - coord[1])
    


 