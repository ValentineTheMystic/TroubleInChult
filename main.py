import pygame
import stateMachine

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

### Initialize pygame
pygame.init()

### Variable objects declared BEFORE the game loop begins
clock = pygame.time.Clock()
state = stateMachine.State()
state.displayWorldMap()
#markerOneSurf = pygame.Surface((50,50))
#markerOneRect = pygame.draw.circle(markerOneSurf,(255,255,255),(100,100),50)
#markerOneRect = pygame.Rect(100,100,50,50)
### Main loop
running = True # While set to true the game will continue to play

while running:
 for event in pygame.event.get(): # Loop through the event queue
  if event.type == KEYDOWN:
   print("keydown")
   if event.key == K_SPACE: # If the Esc key is pressed exit the main loop
    state.endTurn()
    print(state.gameDay)
   if event.key == K_ESCAPE: # If the Esc key is pressed exit the main loop
    running = False
  elif event.type == QUIT: # Check for QUIT event. If QUIT, then set running to false and exit main loop.
   running = False
 pressed_keys = pygame.key.get_pressed() # Get all keys currently pressed
 state.screen.blit(state.worldMapBG,(0, 0)) # Draw the background to the screen
 state.screen.blit(state.worldMapHud,state.worldMapHudRect)
# state.screen.blit(markerOneSurf,(100,100))
 state.updateWorldMap()
 pygame.display.flip()  # Update the display
 clock.tick(30) # Insure the program maintains a constant framerate(30FPS)
