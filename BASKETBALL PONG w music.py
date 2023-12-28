import pygame
import sys
from pygame.locals import *
from pygame import mixer

"""UPDATE
    LA LABORATOR 21.11
        am modificat vitezele mingii si a paletelor
        pentru a-l face jucabil
        de asemenea oponentul acum se misca dupa minge si nu cu o secventa repetata"""
def Game():
   #dimensiuni fereastra
    WIDTH=750
    HEIGHT=430

    pygame.display.set_caption("CLASSIC PONG- BASKETBALL THEME")
    screen=pygame.display.set_mode((WIDTH, HEIGHT))
    #background set

    background=pygame.image.load("background.jpg")
    #screen.blit(background, (0,0))

    #coordonate paleta
    color = (255,255,0)
    vel=2
    x=50
    y=50
    width=10
    height=45
    
    player = pygame.Rect(x,y,width,height)
    scorplay=0

    #coordonate minge
    ball = pygame.image.load('ball.png')
    ball_rect = ball.get_rect(center = (WIDTH // 2, HEIGHT // 2))
    ballspeedx=2
    ballspeedy=2
    
    #coordonate oponent
    x2=700
    y2=200
    opponent=pygame.Rect(x2,y2,width,height)
    vel2=1.6
    scoroppo=0

    #main game loop
    run=True
    while run:
        #delay ca sa mearga mingea mai incet; altfel o ia braila
        pygame.time.delay(4)
        
        #background
        screen.fill((70, 147, 229))
        screen.blit(background, (5,0))
        
        #fileu
        #pygame.draw.rect(fereastra, (culoare rgb), (axa x, axa y, latime, inaltime))
        pygame.draw.rect(screen, (255,255,255) ,(375,0, 15, 430))
        pygame.draw.rect(screen, (0,0,0) ,(381,0, 3, 430))

        #declara minge
        screen.blit(ball, ball_rect)

        #declara paleta 1 si 2
        play= pygame.draw.rect(screen, color,(x,y,width,height))
        oppo= pygame.draw.rect(screen,color, (x2, y2, width, height))

        #press key
        key=pygame.key.get_pressed()
        
        #movement y axis player

        if key[pygame.K_w]==True and y>vel:
            y-=vel
        if key[pygame.K_s]==True and y< 430-height-vel:
            y+=vel

            
        #movement opponent 
        if oppo.top<ball_rect.top and y2<430-height-vel2:
            y2+=vel2
        elif oppo.bottom > ball_rect.bottom:
            y2-=vel2
            
        if y2>vel2:
           y2-=vel2
        if  y2< 430-height-vel2:
            y2+=vel2
        


            
        #ball movement
            
        ball_rect.x += ballspeedx
        ball_rect.y +=ballspeedy

        if ball_rect.top <= 0 or ball_rect.bottom >= HEIGHT:
            ballspeedy *= -1

            
        if ball_rect.left <= 0 or ball_rect.right >= (WIDTH-0):
            ballspeedx *= -1


        #collisions  
        collide= pygame.Rect.colliderect(play, ball_rect)
        collide2= pygame.Rect.colliderect(oppo, ball_rect)
        if collide or collide2:
            ballspeedx*=-1

        #walls collisions; walls = liniile subtiri din spatele paletelor, mai exact wall si wall2:   
        wall=pygame.draw.rect(screen, (0,0,0), (35,0,1,440))
        wall2=pygame.draw.rect(screen, (0,0,0), (720,0,1,440))
        
        collidewallplay=pygame.Rect.colliderect(wall, ball_rect)
        collidewalloppo=pygame.Rect.colliderect(wall2, ball_rect)
       
        if collidewalloppo:
            ball_rect = ball.get_rect(center = (WIDTH // 2, HEIGHT // 2))
            pygame.time.delay(800)
            scorplay+=1         #ASTA E VARIABILA IN CARE SE ADUNA PUNCTAJUL TAU
            print("PLAYER: ",scorplay)

        if collidewallplay:
            ball_rect = ball.get_rect(center = (WIDTH // 2, HEIGHT // 2))
            pygame.time.delay(800)
            scoroppo+=1        #ASTA E VARIABILA IN CARE SE ADUNA PUNCTAJUL OPONENTULUI
            print("OPPO: ", scoroppo)

            
        #quit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()





### APELAREA FUNCTIILOR ###
        
pygame.init()


###MUSIC###
mixer.init()
mixer.music.load('DENIS-SPORTS.mp3')
mixer.music.play()




Game()


pygame.quit()
