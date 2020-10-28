import pygame
from GameState import gameState

class Scoreboard:
    score = 0

    def __init__(self, drawCtx):
        self.drawCtx = drawCtx
        self.fontCtx = pygame.font.SysFont("Times New Roman", 40)

    def draw(self):
        self.renderScore()

    def renderScore(self):
        currentScore = self.fontCtx.render(str(gameState['score']), 1, (255,255,255))
        self.drawCtx.blit(currentScore, (20, 20))


