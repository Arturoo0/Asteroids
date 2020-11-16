import pygame
import Draw
from GameState import gameState

class Scoreboard:
    score = 0

    def __init__(self, drawCtx):
        self.drawCtx = drawCtx
        self.fontCtx = pygame.font.SysFont("Times New Roman", 40)
        self.lifePolyBaseCoords = [[700, 25], [690, 45], [710, 45]]
        self.lifeShift = 25

    def draw(self):
        self.renderScore()
        self.renderLives()

    def renderScore(self):
        currentScore = self.fontCtx.render(str(gameState['score']), 1, (255,255,255))
        self.drawCtx.blit(currentScore, (20, 20))
    
    def renderLives(self):
        coordCopy = [coord[:] for coord in self.lifePolyBaseCoords]
        for life in range(gameState['lives']):
            Draw.drawPolygon(self.drawCtx, (255,255,255), coordCopy, fillType=1)
            for coord in coordCopy:
                coord[0] += self.lifeShift



