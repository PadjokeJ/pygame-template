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
fps = 60


while game:
    clock.tick(fps)

    #all inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            break

    
    #end of loop
    pygame.display.flip()

pygame.quit()
