# Kristofer Nagaicevs IS24 19.04.25

import pygame, random # importib teegid
pygame.init() # initialiseerib pygame-i

### TAUSTAMUUSIKA LISAMINE ###
pygame.mixer.music.load('harjutus6/music/bg.mp3') # laeb muusikafaili 
pygame.mixer.music.play(-1) # mängib lõpmatult
 
### MUUTUJAD ###

# algne taustavärv (punane)
bg_color = [255, 200, 200]

# kõik taustavärvid
lRed = [255, 200, 200]
lOrange = [255, 215, 200]
lYellow = [255, 255, 200]
lGreen = [200, 255, 200]
lCyan = [200, 255, 255]
lBlue = [200, 200, 255]
lPurple = [255, 200, 255]
gray = [100, 100, 100]
# must värv tekstiks
black = [0, 0, 0]
 
# skooride muutujate määramine
punktid = 0
highscore = 0

# palli positsiooni muutujad
posX, posY = random.randint(0,50), random.randint(0,50)
speedX, speedY = 3, 2

# aluse positsiooni muutujad
posX2 = 250
speedX2 = 3

# määrab skoori fonti ja suuruse
font = pygame.font.Font(pygame.font.match_font('sansserif'), 32)

# game over ekraani tekst
gameover = font.render("Mäng läbi! Vajuta Enter, et uuesti proovida", True, [255,255,255]) # määrab teksti ja atribuudid
gameover2 = font.render("Või vajuta Escape, et väljuda.", True, [255,255,255]) # määrab teksti ja atribuudid
finalscore = font.render(f"Sinu skoor: {punktid}", True, [0,0,0]) # määrab teksti ja atribuudid

### EKRAANI SEADED ###

screenX = 640 # laius
screenY = 480 # kõrgus
screen = pygame.display.set_mode([screenX,screenY])
pygame.display.set_caption("Ping-pong täiendatud")
screen.fill(bg_color)
clock = pygame.time.Clock()

### OBJEKTIDE LOOMINE ###

# Palli loomine
ball = pygame.Rect(posX, posY, 20, 20) # määrab palli atribuudid
ball_img = pygame.image.load("harjutus6/img/ball-1.png") # määrab palli pildi
ball_img = pygame.transform.scale(ball_img, [ball.width, ball.height]) # määrab palli pildi mõõtmed palli ristkülikul

# Aluse loomine
pad = pygame.Rect(posX2, screenY/1.5, 120, 20) # määrab aluse atribuudid
pad_img = pygame.image.load("harjutus6/img/pad.png") # määrab aluse pildi
pad_img = pygame.transform.scale(pad_img, [pad.width, pad.height]) # määrab palli pildi mõõtmed aluse ristkülikul

### MÄNGU TSÜKKEL ###
playing = True
fps = 120 # määrab mängu kiiruse

running = True
while running:
    clock.tick(fps) # mängu kiirus
    for event in pygame.event.get():
       if event.type == pygame.QUIT: # võimaldab ristist kinni panemise
           running = False

    # kui mäng ei käi, ehk kui mäng on läbi
    if playing == False:
            if punktid > highscore: # top skoori lugemine määramine
                highscore = punktid

            # gameover ekraani taust
            screen.fill(gray)

            screen.blit(gameover, [100,100]) # kuvab teksti ekraanil
            screen.blit(gameover2, [100,130]) # kuvab teksti ekraanil
            finalscore = font.render(f"Sinu skoor: {punktid}", True, [0,0,0]) # määrab teksti ja atribuudid
            screen.blit(finalscore, [100,190]) # kuvab teksti ekraanil
            highscoretext = font.render(f"Sinu kõrgeim skoor: {highscore}", True, [0,0,0]) # määrab teksti ja atribuudid
            screen.blit(highscoretext, [100,220]) # kuvab teksti ekraanil

            # tuvastab klahvi vajutusi
            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_ESCAPE]: # esc vajutamisel
                running = False # paneb mängu kinni

            if pressed[pygame.K_RETURN]: # enter klahvi vajutamisel
                
                punktid = 0 # resettib punktid
                bg_color = lRed # resettib tausta värvi
                fps = 120 # resettib mängu kiiruse

                # resettib palli ja aluse kordinaadid ja tä
                posX, posY = random.randint(0,50), random.randint(0,50)
                posX2 = 250
                pad = pygame.Rect(posX2, screenY/1.5, 120, 20)

                playing = True # käivitab mängu loopi
                
    elif playing == True: # kui mäng käib, ehk kui mängija tahtis (uuesti) mängida

        ### PALLI LIIKUMINE ###
        ball = pygame.Rect(posX, posY, 20, 20)
        screen.blit(ball_img,ball)

        # liigub alguses alla paremale
        posX += speedX
        posY += speedY

        # paneb palli põrkama vastu ekraani ääri
        if posX > screenX-ball_img.get_rect().width or posX < 0: 
            speedX = -speedX
        if posY < 0:
            speedY = -speedY
        # kui pall puudutab ekraani alumist äärt, siis mäng läheb kinni
        if posY > screenY-ball_img.get_rect().height: 
            playing = False

        ### ALUSE LIIKUMINE ###

        pressed = pygame.key.get_pressed()
        # klahvi vajutusel liigub alus
        if pressed[pygame.K_LEFT]:
            posX2 -= 6
            pad = pygame.Rect(posX2, screenY/1.5, 120, 20)
        if pressed[pygame.K_RIGHT]:
            posX2 += 6
            pad = pygame.Rect(posX2, screenY/1.5, 120, 20)

        # kontrollib, kas alus on ekraani piirides ja piirab sisse
        if posX2 < 0:
            posX2 = 0
        if posX2 > 520:
            posX2 = 520


        # kui pall puudutab alust
        if ball.colliderect(pad):
            if speedY > 0: # kontrollib, kas liigub alla pall
                speedY = -speedY # põrkab
                punktid += 1 # lisab skoorile punkti juurde


        ### SKOORI PÕHJALT MÄNGU KIIRENDAMINE JA TAUSTA MUUTMINE ###

        if punktid >= 10: # kui punktide arv on 10 või rohkem
            bg_color = lOrange # muudab tausta värvi
            fps = 140 # teeb mängu kiiremaks
        if punktid >= 20: 
            bg_color = lYellow 
            fps = 160 
        if punktid >= 30: 
            bg_color = lGreen
            fps = 180 
        if punktid >= 40: 
            bg_color = lCyan 
            fps = 200 
        if punktid >= 50: 
            bg_color = lBlue 
            fps = 220 
        if punktid >= 60:
            bg_color = lPurple 
            fps = 240

        ### SKOORI KUVAMINE ###
        
        text = font.render(f"Skoor: {punktid}", True, [0,0,0]) # määrab teksti ja atribuudid
        screen.blit(text, [0,0]) # kuvab teksti ekraanil
        screen.blit(pad_img,pad) # kuvab aluse ekraanil

    pygame.display.flip() # graafika kuvamine ekraanil
    screen.fill(bg_color) # värvib taustavärviga ekraani üle peale igat frame-i, et ei tekiks rada peale igat liikumist