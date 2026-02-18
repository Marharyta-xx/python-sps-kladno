# import pygame package
import pygame

# initializing imported module
pygame.init()
icon = pygame.image.load('obrazky/icon.jpg')
# displaying a window of height
# 500 and width 400
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((400,500))
color1 = "red"
color = (255,255,0)


# creating a bool value which checks
# if game is running
running = True

# keep game running till running is true
while running:
    
    # Check for event if user has pushed
    # any event in queue
    for event in pygame.event.get():
        
        # if event is of type quit then 
        # set running bool to false
        if event.type == pygame.QUIT:
            running = False
    screen.fill(color1)
    screen.blit(icon, (70,30))

    pygame.draw.rect(screen, color, 
                 pygame.Rect(30, 30, 60, 60))

    pygame.display.flip()
            