from GameState import gameState
import Draw
import pygame

class Menu: 

	def __init__(self, drawCtx):
		self.drawCtx = drawCtx
		self.fontCtx = pygame.font.SysFont("Times New Roman", 60)
		self.startButtonWidth = 300
		self.startButtonHeight = 95
		self.startButtonTopLeft = ((400 - (self.startButtonWidth//2)), 400)
		self.startText = self.fontCtx.render('Start' , 1, (255,255,255))
		self.startTextTopLeft = (400 - (self.startText.get_width()//2), (self.startButtonTopLeft[1] * 2 + self.startButtonHeight)//2 - (self.startText.get_height()//2))

	def draw(self):
		self.drawStartButtonText()
		self.drawStartButton()

	def drawStartButtonText(self):
		x, y = self.startTextTopLeft
		self.drawCtx.blit(self.startText, (x, y))

	def drawStartButton(self):
		x, y = self.startButtonTopLeft
		height = self.startButtonHeight
		width = self.startButtonWidth
		Draw.drawRect(self.drawCtx, (255, 255, 255), (x, y, width, height), fillType=1)
