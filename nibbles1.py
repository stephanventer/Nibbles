import pygame
#initialize pygame
pygame.init()
pygame.font.init()

#set up the screen and screen size
screen = pygame.display.set_mode((700,700))

#define variables
worm_x = [350,330,310,290]
worm_y = [350,350,350,350]
wormblocksize = 20;

up = False;
down = False;
left = False;
right = False;

#write some text
def writetext(text, x, y, color=(0,0,0), fontsize=24):
    # you have to call this at the start, 
    myfont = pygame.font.SysFont('Arial', fontsize, False, False)
    textsurface = myfont.render(text, True, color)
    screen.blit(textsurface, (x, y))

#draw worm
def drawworm(wrm_x, wrm_y):
    for i in range(len(worm_x)):
        #draw worm shadow
        pygame.draw.circle(screen, (77, 0, 77), (worm_x[i]-1, worm_y[i]+2), 15)

    for i in range(len(worm_x)):
        #draw worm body
        pygame.draw.circle(screen, (153, 0, 153), (worm_x[i], worm_y[i]), 15)



#initialize the main game loop
running = True
while running:
    #fill background
    screen.fill((92, 230, 131))

    #speed of game
    pygame.time.delay(70)

    #go through events and see if close button was click
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if(right):
                    pass
                else:
                    left = True
                    right, up, down = False, False, False
            elif event.key == pygame.K_RIGHT:
                if(left):
                    pass
                else:
                    right = True
                    left, up, down = False, False, False
            elif event.key == pygame.K_UP:
                if(down):
                    pass
                else:
                    up = True
                    right, left, down = False, False, False
            elif event.key == pygame.K_DOWN:
                if(up):
                    pass
                else:
                    down = True
                    right, left, up = False, False, False
    
 
    #draw a purple circle
    #circle1 = pygame.draw.circle(screen, (204, 51, 255), (posx, posy), 20)
    drawworm(worm_x, worm_y)

    #move worm in direction
    if(right):
        worm_x.insert(0, worm_x[0] + wormblocksize)
        worm_x.pop()
        worm_y.insert(0, worm_y[0])
        worm_y.pop()

    if(left):
        worm_x.insert(0, worm_x[0] - wormblocksize)
        worm_x.pop()
        worm_y.insert(0, worm_y[0])
        worm_y.pop()

    if(down):
        worm_x.insert(0, worm_x[0] )
        worm_x.pop()
        worm_y.insert(0, worm_y[0] + wormblocksize)
        worm_y.pop()

    if(up):
        worm_x.insert(0, worm_x[0])
        worm_x.pop()
        worm_y.insert(0, worm_y[0] - wormblocksize)
        worm_y.pop()

    #draw a red line
    #pygame.draw.line(screen, (255, 153, 51), (30, 400), (670, 500), 5)
    #add some text
    #writetext('My Awesome Game', 0, 0)
    #writetext('The is the second line', 0, 100, (255,0,0))
    #writetext('And the third line', 0, 200, (0,0,255), 48)
    
    #update the game screen with latest
    pygame.display.update()
pygame.quit()