import pygame
from pygame.locals import * # Constants
#VARIABLEN

WHITE =     (255, 255, 255)
BLUE =      (  0,   0, 255)
YELLOW =    (255,255,0)
GREEN =     (  0, 255,   0)
RED =       (255,   0,   0)
BLACK = (  0,   0,  0)

ZOOM = 100 # eine Einheit = PIXEL
ANZAHL = 5 # Anzahl der Spielfeldeinheiten
RAND_X = 1 #Anzahl der RANDeinheiten
RAND_Y = 1 

Fenster_X = ZOOM * (ANZAHL + 2 * RAND_X)
Fenster_Y = ZOOM * (ANZAHL + 2 * RAND_Y)

Spielfeld_X = ZOOM * RAND_X
Spielfeld_Y = ZOOM * RAND_Y
Spielfeld_Breite = ZOOM * ANZAHL
Spielfeld_Hoehe = ZOOM * ANZAHL
Spielfeld_Farbe =BLUE
Spielfeld = [Spielfeld_X, Spielfeld_Y, Spielfeld_Breite, Spielfeld_Hoehe]

Stein_Radius = 0.4

screen = pygame.display.set_mode((Fenster_X, Fenster_Y))
pygame.display.set_caption("N  I  L  S")
screen.fill((BLACK))
pygame.draw.rect(screen, Spielfeld_Farbe, Spielfeld)

#RASTER
#Zeichne Waagerechtes Raster
Raster_Farbe = WHITE
x1 = ZOOM * RAND_X
y1 = ZOOM * RAND_Y
p1 = [x1,y1]
x2 = ZOOM * (RAND_X + ANZAHL)
y2 = y1
p2 = [x2,y2]
for i in range(ANZAHL + 1):
    pointlist = [p1,p2]
    pygame.draw.lines(screen, Raster_Farbe, False, pointlist)
    y1 = y1 +ZOOM 
    y2 = y2 + ZOOM
    p1 = [x1,y1]
    p2 = [x2,y2]
#Zeichne Senkrechtes Raster    
x1 = ZOOM * RAND_X
y1 = ZOOM * RAND_Y
p1 = [x1,y1]
x2 = x1
y2 = ZOOM * (RAND_Y + ANZAHL)
p2 = [x2,y2]
for i in range(ANZAHL + 1):
    pointlist = [p1,p2]
    pygame.draw.lines(screen, Raster_Farbe, False, pointlist)
    x1 =  x1 + ZOOM
    x2 = x2 + ZOOM
    p1 = [x1,y1]
    p2 = [x2,y2]


for Zeile in range(ANZAHL):
    for Spalte in range(ANZAHL):
        y = int(ZOOM * (RAND_Y + ANZAHL - 0.5 - Zeile))
        x = int(ZOOM * (RAND_X + Spalte + 0.5))
        pm =[x,y]
        radius = int(Stein_Radius * ZOOM)
        pygame.draw.circle(screen, YELLOW, pm, radius)






pygame.display.update()
GameOver = False
while not(GameOver):

    for e in pygame.event.get():
        if e.type == KEYDOWN:
            key = e.key
            if key == K_DOWN:
                pygame.quit(); exit()
            if key == K_UP:
                q1=(0,0,Fenster_X, int(ZOOM *RAND_Y))
                
                q2=(0,0,int(ZOOM *RAND_Y),Fenster_Y)
               
                q3=(ZOOM*(RAND_X + ANZAHL),0,ZOOM* RAND_X, Fenster_Y)
               
                q4=(0,ZOOM*(RAND_Y + ANZAHL),Fenster_X,RAND_Y*ZOOM)
                pygame.draw.rect(screen, RED, q1)
                pygame.draw.rect(screen, RED, q2)
                pygame.draw.rect(screen, RED, q3)
                pygame.draw.rect(screen, RED, q4)
                pygame.display.update()

            
               


 