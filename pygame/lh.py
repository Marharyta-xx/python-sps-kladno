import pygame
import sys
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((600, 600))
a = 50
b = 200
run = True
vlevo = False
ball = pygame.image.load('R.png')
ball = pygame.transform.scale(ball,(40,40))
rotang = 0


while run:
    clock.tick(60)
    window.fill(0,0,0)
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    rotatedball = pygame.transform.rotate(ball, rotang )
    ballrect = rotatedball.get_rect(center = (a,b))
    window.blit(rotatedball, ballrect)
    pygame.draw.line(window, (255, 102, 0), 
                 [100, 300], 
                 [500, 300], 5)
    if vlevo:
        a -= 1
        rotang += 5
        if a <=50:
            vlevo = False
    else:
        a+=1
        rotang -= 15
        if a>350:
            vlevo = True

    pygame.display.flip()
pygame.quit()
