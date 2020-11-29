from GameState import gameState
import Draw
import pygame
import starfield

class Menu: 

	def __init__(self, drawCtx):
		self.drawCtx = drawCtx
		self.fontCtx = pygame.font.SysFont("Times New Roman", 60)
		self.asteroidFontCtx = pygame.font.SysFont("Times New Roman", 120)
		self.startButtonWidth = 300
		self.startButtonHeight = 95
		self.startButtonTopLeft = ((400 - (self.startButtonWidth//2)), 400)
		self.startText = self.fontCtx.render('Start' , 1, (255,255,255))
		self.asteroidsText = self.asteroidFontCtx.render('Asteroids' , 1, (255,255,255))
		self.startTextTopLeft = (400 - (self.startText.get_width()//2), (self.startButtonTopLeft[1] * 2 + self.startButtonHeight)//2 - (self.startText.get_height()//2))
		self.asteroidsTextTopLeft = (400 - (self.asteroidsText.get_width()//2), 200)
		self.isHovering = False
		self.starfield = starfield.Starfield(drawCtx, 200)

	def draw(self):
		self.drawStartButtonText()
		self.drawStartButton()
		self.drawAsteroidsText()
		self.starfield.draw()
	
	def update(self, dt):
		self.hoveringOverButton()
		self.starfield.update(dt)
			
	def trackKeyPresses(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			x, y = pygame.mouse.get_pos()
			xCheck = x >= self.startButtonTopLeft[0] and x <= self.startButtonTopLeft[0] + self.startButtonWidth
			yCheck = y >= self.startButtonTopLeft[1] and y <= self.startButtonTopLeft[1] + self.startButtonHeight
			if xCheck and yCheck: gameState['inMenu'] = False
	
	def drawHoverEffect(self):
		x, y = self.startButtonTopLeft
		if self.isHovering:
			for i in range(20):
				offset = (i//2)
				Draw.drawRect(self.drawCtx, (255, 255, 255), (x - offset, y - offset, self.startButtonWidth, self.startButtonHeight), fillType=1)

	def hoveringOverButton(self):
		x, y = pygame.mouse.get_pos()
		xCheck = x >= self.startButtonTopLeft[0] and x <= self.startButtonTopLeft[0] + self.startButtonWidth
		yCheck = y >= self.startButtonTopLeft[1] and y <= self.startButtonTopLeft[1] + self.startButtonHeight
		if xCheck and yCheck:
			self.isHovering = True
		else: self.isHovering = False
		self.drawHoverEffect()

	def drawAsteroidsText(self):
		x, y = self.asteroidsTextTopLeft
		self.drawCtx.blit(self.asteroidsText, (x, y))

	def drawStartButtonText(self):
		x, y = self.startTextTopLeft
		self.drawCtx.blit(self.startText, (x, y))
			
	def drawStartButton(self):
		x, y = self.startButtonTopLeft
		height = self.startButtonHeight
		width = self.startButtonWidth
		Draw.drawRect(self.drawCtx, (255, 255, 255), (x, y, width, height), fillType=1)
