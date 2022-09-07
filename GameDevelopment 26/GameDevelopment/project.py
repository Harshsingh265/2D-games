
import pygame
import random
import sys
pygame.init()

SIZE = WIDTH, HEIGHT = 1100,600
#game window
SCREEN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Welcome to Space Invaders Game by:- HARSH AND ANUBHAV")

#colors
RED_COLOR = 255,0,0
BLACK_COLOR = 0,0,0
WHITE_COLOR = 255,255,255
BLUE_COLOR = 0,0,255

#game sound
bg_music = pygame.mixer.Sound("theme.ogg")
bg_music.play()

# image
bgimg= pygame.image.load("bgi.png")
bgimg= pygame.transform.scale(bgimg, (SIZE)).convert_alpha()


move_x = 0

#ship image load
ship = pygame.image.load("player.png")
ship_w = ship.get_width()
ship_h = ship.get_height()
ship_x = (WIDTH // 2) - (ship_w // 2)
ship_y = HEIGHT - ship_h - 10

#enemy ship image load
enemy_ship = pygame.image.load("enemy 1.png")
enemy_w = enemy_ship.get_width()
enemy_h = enemy_ship.get_height()

enemyList = []
rows = 3
cols = WIDTH // enemy_w - 1
enemyRect = []

for i in range(rows):
    for j in range(cols):
        rect_x = (enemy_w + 5) * j
        rect_y = (enemy_h + 5) * i
        enemyList.append([rect_x, rect_y])
        enemyRect.append(pygame.Rect(rect_x, rect_y, enemy_w, enemy_h))

#bullet
bullet_sound = pygame.mixer.Sound("sound_3.wav")

bullet_w = 10
bullet_x = ship_x + (ship_w // 2) - (bullet_w // 2)
bullet_y = ship_y
move_bullet = 0

clock = pygame.time.Clock()

# mess font
font = pygame.font.SysFont(None, 55)
def mesg(text, colour, x, y ):
    score_text = font.render(text, True, colour)
    SCREEN.blit(score_text, [x,y])
    
def welcome():
    exit_game = False
    
    while not exit_game:
        
        SCREEN.blit(bgimg, (0, 0))
        mesg("Welcome To Space Invaders", WHITE_COLOR, 100, 175)
        mesg("Press Enter To Play", WHITE_COLOR, 100, 225)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()   # quit pygame
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop()
        clock.tick(60)
        pygame.display.update()

def gameloop():
    global bullet_w, bullet_x, bullet_y, move_bullet, move_x, ship_x, ship_y, ship_w, ship_h
    exit_game=False
    game_over=False
    enemyList = []
    rows = 3
    cols = WIDTH // enemy_w - 1
    enemyRect = []

    for i in range(rows):
        for j in range(cols):
            rect_x = (enemy_w + 5) * j
            rect_y = (enemy_h + 5) * i
            enemyList.append([rect_x, rect_y])
            enemyRect.append(pygame.Rect(rect_x, rect_y, enemy_w, enemy_h))
    
    while not exit_game:
        if game_over:
            
            
            SCREEN.blit(bgimg, (0, 0))
            mesg("Game Over!.. ", WHITE_COLOR, 50, 200)
            mesg("Press Enter to continue",WHITE_COLOR,50 ,250)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()   # quit pygame
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
            clock.tick(60)
            pygame.display.update()
            
        else:
            bullet_x = ship_x + (ship_w // 2) - (bullet_w // 2)
            # Events
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()   # quit pygame
                    quit()  # quit python

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        move_x = 1
                        
                    elif event.key == pygame.K_LEFT:
                        move_x = -1
                        
                    elif event.key == pygame.K_SPACE:
                        move_bullet = -50
                        bullet_sound.play()
                else:
                    move_x = 0

            SCREEN.fill(BLUE_COLOR)

            for i in range(len(enemyList)):
                SCREEN.blit(enemy_ship, 
                (enemyList[i][0], enemyList[i][1]))
            
            bullet_rect = pygame.draw.rect(SCREEN, RED_COLOR, 
            [bullet_x, bullet_y, bullet_w, bullet_w])
            SCREEN.blit(ship, (ship_x, ship_y))
            
            
            if ship_x > 0 and ship_x<990:
                ship_x += move_x
            elif ship_x <= 0:
                ship_x=1
            elif ship_x >=990:
                ship_x=989
                
            bullet_y += move_bullet
            

            for i in range(len(enemyRect)):
                if bullet_rect.colliderect(enemyRect[i]):
                    del enemyRect[i]
                    del enemyList[i]
                    bullet_y = ship_y
                    move_bullet = 0
                    break

            if bullet_y < 0:
                bullet_x = ship_x + (ship_w // 2) - (bullet_w // 2)
                bullet_y = ship_y
                move_bullet = 0
                
            if enemyList == []:
                game_over=True
            
            # to update the screen
            pygame.display.flip()

    #end screen
    

welcome()
        

