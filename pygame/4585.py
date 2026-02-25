# import pygame module in this program 
import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Jump Game")

x = 200
y = 200
width = 40
height = 40
isjump = False
v = 5
m = 1
run = True
vel = 10
ctv = pygame.Rect(x,y, width, height )
cara1rec = pygame.Rect(100,200+height, 250, 2)
cara2rec = pygame.Rect(400,200+height*3, 500, 2)

while run:

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            run = False
    keys = pygame.key.get_pressed() 
	
      
    if isjump == False:
 
        # if space bar is pressed
        if keys[pygame.K_SPACE]:
            isjump = True
             
    if isjump :
        # calculate force (F). F = 1 / 2 * mass * velocity ^ 2.
        F =(1 / 2)*m*(v**2)
        y-= F
        v = v-1
        if v<0:
            m =-1
            if cara1rec.colliderect(ctv):
                isjump = False
                v = 7-1
                m = 1
                ctv.bottom = cara1rec.top +1
            if cara2rec.colliderect(ctv):
                isjump = False
                v = 7-1
                m = 1
                ctv.bottom = cara1rec.top +1
        if v ==-6:
            isjump = False
            v = 5
            m = 1
    if keys[pygame.K_LEFT] and x>0: x -= vel 
    if keys[pygame.K_RIGHT] and x<500-width:x += vel 
    # creates time delay of 10ms
    pygame.draw.line(win, (255, 108, 255), 
                 [0, 240], 
                 [250, 240], 5)
    pygame.draw.line(win, (255, 1, 245), 
                 [350, 300], 
                 [600, 300], 5)
    pygame.time.delay(25)
 
    # it refreshes the window
    pygame.display.update() 
# closes the pygame window    
pygame.quit()