import sys
import pygame



screen_width =  640
screen_height = 480

white =(255,255,255)
black =(0,0,0)


pygame.init()
pygame.display.set_caption("Simple pygame example")
screen = pygame.display.set_mode((screen_width, screen_height))


x = 200
y =200

clock = pygame.time.Clock()

while True:
    clock.tick (60)

    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    key_event = pygame.key.get_pressed()


#좌측 상단이 (0.0)이므로
    if key_event[pygame.K_LEFT]:
        x-=1
    if key_event[pygame.K_RIGHT]:
        x+=1
    if key_event[pygame.K_DOWN]:
        y+=1
    if key_event[pygame.K_UP]:
        y-=1


    screen.fill(black)
    pygame.draw.circle(screen,white,(x,y),20)
    pygame.display.update()