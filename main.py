import pygame

#initialise pygame
pygame.init()
#screen size
scr = (width, height) = (960, 960)
screen = pygame.display.set_mode((width, height))
#prepare game loop
game = True
#init clock for fps manipulation
clock = pygame.time.Clock()
#feel free to edit the fps of your game
fps = 60


while game:
    #deltaTime is the time taken since that last loop execution, useful for keeping movement regular even when lower or higher framerates are observed
    deltaTime = clock.tick(fps) / 1000 

#all inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # ends the game, can be a different key if desired. The program will run fine without this
                game = False
                break
#            if event.key == pygame.K_<keyname>:
#                <put your logic here>
    #end of loop
    pygame.display.flip() #updates the screen to show any graphical changes

pygame.quit()
