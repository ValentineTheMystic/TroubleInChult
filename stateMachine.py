import pygame

from pygame.locals import (
    RLEACCEL,
#    K_p,
#    K_UP,
#    K_DOWN,
#    K_LEFT,
#    K_RIGHT,
#    K_ESCAPE,
#    KEYDOWN,
#    QUIT,
)

## These Variables control the size of the pygame window
width = 650
height = 700
color_dark = (100,100,100)

class State():
 def __init__(self):
  self.screen = pygame.display.set_mode((width,height))
  self.location = 0
  self.gameDay = 0

 def displayWorldMap(self):
  self.worldMapBG = pygame.image.load("assets/chultMap.png").convert()
  self.worldMapBG.set_colorkey((255,255,255),RLEACCEL)
  self.worldMapHud = pygame.Surface((300,75))
  self.worldMapHud.fill((255,255,255))
  self.worldMapHudRect = pygame.Rect(400,0,300,75)
  self.headerFont = pygame.font.SysFont("Verdana", 20)

 def updateWorldMap(self):
  hudText = self.headerFont.render("Day:" + str(self.gameDay),True,color_dark)
  self.screen.blit(hudText,(410,10))

 def displayMainMenu(self):
  self.worldMapBG = pygame.image.load("assets/chultMap.png").convert()
  self.worldMapBG.set_colorkey((255,255,255),RLEACCEL)
  self.worldMapHud = pygame.Surface((300,75))
  self.worldMapHud.fill((255,255,255))
  self.worldMapHudRect = pygame.Rect(400,0,300,75)
  self.headerFont = pygame.font.SysFont("Verdana", 20)

 def updateMainMenu(self):
  hudText = self.headerFont.render("Day:" + str(self.gameDay),True,color_dark)
  self.screen.blit(hudText,(410,10))

 def displayPartyMenu(self):
  self.worldMapBG = pygame.image.load("assets/chultMap.png").convert()
  self.worldMapBG.set_colorkey((255,255,255),RLEACCEL)
  self.worldMapHud = pygame.Surface((300,75))
  self.worldMapHud.fill((255,255,255))
  self.worldMapHudRect = pygame.Rect(400,0,300,75)
  self.headerFont = pygame.font.SysFont("Verdana", 20)

 def updatePartyMenu(self):
  hudText = self.headerFont.render("Day:" + str(self.gameDay),True,color_dark)
  self.screen.blit(hudText,(410,10))


 def endTurn(self):
  self.gameDay += 1
