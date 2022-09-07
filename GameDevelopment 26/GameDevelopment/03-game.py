import pygame
import random
pygame.init()

SIZE = WIDTH, HEIGHT = 1000,600

SCREEN = pygame.display.set_mode(SIZE)

RED_COLOR = 255,0,0
BLACK_COLOR = 0,0,0
WHITE_COLOR = 255,255,255
BLUE_COLOR = 0,0,255

rect_x = 0
rect_y = 0
rect_w = 50
rect_h = 50

move_x = 0
move_y = 0

while True:

    # Events
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()   # quit pygame
            quit()  # quit python

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_x = 0.3
            elif event.key == pygame.K_LEFT:
                move_x = -0.3
        else:
            move_x = 0

    SCREEN.fill(WHITE_COLOR)

    pygame.draw.rect(SCREEN, RED_COLOR, 
    [rect_x, rect_y, rect_w, rect_h])

    rect_x += move_x
    rect_y += move_y

    if rect_x > WIDTH - rect_w:
        move_x = -0.3
    elif rect_x < 0:
        move_x = 0.3

    if rect_y > HEIGHT - rect_h:
        move_y = -0.3
    elif rect_y < 0:
        move_y = 0.3

    # to update the screen
    pygame.display.flip()