import pygame 

def drawRect(display, color, drawCoords, fillType=0):
    pygame.draw.rect(display, color, drawCoords, fillType)

def drawPolygon(display, color, points, fillType=0):
    pygame.draw.polygon(display, color, points, fillType)

