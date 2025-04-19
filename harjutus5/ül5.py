# Kristofer Nagaicevs IS24 19.04.25

import pygame, random # importib teegid
pygame.init() # initialiseerib pygame-i
 
### MUUTUJAD ###

# värvid
bg_color = [200, 255, 200]
red = [255, 0, 0]
black = [0, 0, 0]
green = [0, 200, 0]
textcolor = [0, 0, 0] # muutuv teksti värv
 
# skoori muutuja määramine
punktid = 0

# palli positsiooni muutujad
posX, posY = 0, 0
speedX, speedY = 3, 4

# aluse positsiooni muutujad
posX2 = random.randint(0,500)
speedX2 = 3

# määrab skoori fonti ja suuruse
font = pygame.font.Font(pygame.font.match_font('sansserif'), 32)

### EKRAANI SEADED ###

screenX = 640 # laius
screenY = 480 # kõrgus
screen = pygame.display.set_mode([screenX,screenY])
pygame.display.set_caption("Ping-pong")
screen.fill(bg_color)
clock = pygame.time.Clock()

### OBJEKTIDE LOOMINE ###

# Palli loomine
ball = pygame.Rect(posX, posY, 20, 20) # määrab palli atribuudid
ball_img = pygame.image.load("harjutus5/img/ball-1.png") # määrab palli pildi
ball_img = pygame.transform.scale(ball_img, [ball.width, ball.height]) # määrab palli pildi mõõtmed palli ristkülikul

# Aluse loomine
pad = pygame.Rect(posX2, screenY/1.5, 120, 20) # määrab aluse atribuudid
pad_img = pygame.image.load("harjutus5/img/pad.png") # määrab aluse pildi
pad_img = pygame.transform.scale(pad_img, [pad.width, pad.height]) # määrab palli pildi mõõtmed aluse ristkülikul


### MÄNGU TSÜKKEL ###

running = True
while running:
    clock.tick(180)#fps
    for event in pygame.event.get():
       if event.type == pygame.QUIT: # võimaldab ristist kinni panemise
           running = False


    ### PALLI LIIKUMINE ###
    ball = pygame.Rect(posX, posY, 20, 20)
    screen.blit(ball_img,ball)

    # liigub alguses alla paremale
    posX += speedX
    posY += speedY

    # paneb palli põrkama vastu ekraani ääri
    if posX > screenX-ball_img.get_rect().width or posX < 0: 
        speedX = -speedX
    if posY > screenY-ball_img.get_rect().height or posY < 0:
        speedY = -speedY

    # kui puudutab alumist äärt:
    if posY > screenY-ball_img.get_rect().height:
        punktid -= 1 # lahutab ühe punkti
        textcolor = red # muudab skoori teksti värvi punaseks


    ### ALUSE LIIKUMINE ###

    pad = pygame.Rect(posX2, screenY/1.5, 120, 20)
    screen.blit(pad_img,pad)
    posX2 += speedX2
    # põrkab vastu seina
    if posX2 > screenX-pad_img.get_rect().width or posX2 < 0: 
        speedX2 = -speedX2 

    # kui pall puudutab alust
    if ball.colliderect(pad):
        if speedY > 0: # kontrollib, kas liigub alla pall
            speedY = -speedY # põrkab
            punktid += 1 # lisab skoorile punkti juurde
            textcolor = green # muudab skoori teksti värvi roheliseks


    ### SKOORI KUVAMINE ###
    
    text = font.render(f"Skoor: {punktid}", True, textcolor) # määrab teksti ja atribuudid
    screen.blit(text, [0,0]) # kuvab teksti ekraanil
    
    
    pygame.display.flip() # graafika kuvamine ekraanil
    screen.fill(bg_color) # värvib taustavärviga ekraani üle peale igat frame-i, et ei tekiks rada peale igat liikumist