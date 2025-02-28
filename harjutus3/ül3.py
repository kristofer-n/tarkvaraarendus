# Kristofer Nagaicevs IS24 28.02.25

# import
import pygame

# värvid (koos ekstra värvidega testimiseks)
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
yellow = [255, 255, 0]
black = [0, 0, 0]
white = [255, 255, 255]
lGreen = [153, 255, 153]

# akna loomine
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Ruudud")
screen.fill(lGreen)

# ruudustiku joonistamise funktsioon
def ruudud(width, height, lines, columns, color):

    # määrab muutujad
    x = -1
    y = -1

    # joonistab esimese ruudu 
    pygame.draw.rect(screen,color,[x,y,width,height],2)

    # joonistab ruudustiku
    for i in range(lines): # kordab tsükli sees olevaid juppe nii palju, kui ridu on
        for i in range(columns): # kordab tsükli sees olevaid juppe nii palju, kui veergusid on
            pygame.draw.rect(screen,color,[x,y,width,height],2)
            # joonistab järgmise ruudu täpselt kõrvale
            x += width 
            x -= 2
        # joonistab järgmise ruudu täpselt alla
        x = -1 # toob tagasi vasakule küljele
        y += height
        y -= 2

# kutsub esile funktsiooni koos määratud parameetritega
ruudud(22, 22, 24, 32, red)

# näitab muudatused ekraanil
pygame.display.flip()

# akna lahtipüsimiseks vajalik kood + ristist kinni panemise funktsioon
running = True
while running:
   for event in pygame.event.get():
       # See võimaldab ka mängu ristist kinni panna!
       if event.type == pygame.QUIT:
           running = False
