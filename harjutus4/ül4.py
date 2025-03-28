# Kristofer Nagaicevs IS24 28.03.2025
import pygame, sys, random
pygame.init()
 
#ekraani seaded
screenX = 640
screenY = 480
screen=pygame.display.set_mode([screenX,screenY])
pygame.display.set_caption("Autod")
clock = pygame.time.Clock()

# siniste auto kiirused (alguses alati aeglaselt, et mängijal võimalus mängu alguses mööda sõita
speedY = 1
speedY2 = 1
speedY3 = 1

# autode koordinaatide määramine
autoX = 295
autoY = 350
sinine_autoX = random.randint(150, 225)
sinine_autoY = random.randint(0, 240)
sinine_autoX2 = random.randint(275, 340)
sinine_autoY2 = random.randint(0, 120)
sinine_autoX3 = random.randint(375, 450)
sinine_autoY3 = random.randint(0, 240)

# taustapildi defineerimine
taust = pygame.image.load("harjutus4/img/bg_rally.jpg")

### PUNANE AUTO ###
# loob punase auto ristküliku ning määrab sellele punase auto pildi
punane_auto = pygame.image.load("harjutus4/img/f1_red.png")
punane_auto = pygame.Rect(autoX, autoY, 45, 90)
punane_auto_pilt = pygame.image.load("harjutus4/img/f1_red.png")
punane_auto_pilt = pygame.transform.scale(punane_auto_pilt, [punane_auto.width, punane_auto.height])

### SINISED AUTOD ###

# loovad siniste autode ristkülikud ning määrab sellele siniste autode pildi
sinine_auto = []
for i in range(3):
    sinine_auto.append(pygame.Rect(sinine_autoX, random.randint(0, 240), 45, 90))
sinine_auto_pilt = pygame.image.load('harjutus4/img/f1_blue.png')
sinine_auto_pilt = pygame.transform.scale(sinine_auto_pilt, [sinine_auto[0].width, sinine_auto[0].height])

sinine_auto2 = []
for i in range(3):
    sinine_auto2.append(pygame.Rect(sinine_autoX, random.randint(0, 240), 45, 90))
sinine_auto_pilt2 = pygame.image.load('harjutus4/img/f1_blue.png')
sinine_auto_pilt2 = pygame.transform.scale(sinine_auto_pilt2, [sinine_auto2[0].width, sinine_auto2[0].height])

sinine_auto3 = []
for i in range(3):
    sinine_auto3.append(pygame.Rect(sinine_autoX, random.randint(0, 240), 45, 90))
sinine_auto_pilt3 = pygame.image.load('harjutus4/img/f1_blue.png')
sinine_auto_pilt3 = pygame.transform.scale(sinine_auto_pilt3, [sinine_auto3[0].width, sinine_auto3[0].height])

# tautapildi kuvamine
screen.blit(taust,[0,0])

# punktide muutuja määramine
punktid = 0
highscore = 0

playing = True

font = pygame.font.Font(pygame.font.match_font('sansserif'), 32) # määrab fonti ja suuruse
# game over ekraani tekst
gameover = font.render("Mäng läbi! Vajuta Enter, et uuesti proovida", True, [255,255,255]) # määrab teksti ja atribuudid
gameover2 = font.render("Või vajuta Escape, et väljuda.", True, [255,255,255]) # määrab teksti ja atribuudid
finalscore = font.render(f"Sinu skoor: {punktid}", True, [0,0,0]) # määrab teksti ja atribuudid


# mängu loop
running = True
while running:
    clock.tick(60)#fps
    for event in pygame.event.get():
       if event.type == pygame.QUIT: # võimaldab ristist kinni panemise
           running = False

    if playing == False:
        if punktid > highscore: # top skoori lugemine määramine
            highscore = punktid

        # gameover ekraani taust
        lBlue = [153, 204, 255]
        screen.fill(lBlue)

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

            # resettib siniste autode kordinaadid
            sinine_autoX = random.randint(150, 225)
            sinine_autoY = random.randint(0, 240)
            sinine_autoX2 = random.randint(275, 340)
            sinine_autoY2 = random.randint(0, 120)
            sinine_autoX3 = random.randint(375, 450)
            sinine_autoY3 = random.randint(0, 240)

            # resettib punase auto koordinaadid
            autoX = 295
            punane_auto = pygame.Rect(autoX, autoY, 45, 90)

            playing = True # käivitab mängu loopi
            
    elif playing == True: # kui mäng käib
        ### punase auto liikuma panemine ###
        
        # tuvastab klahvi vajutusi
        pressed = pygame.key.get_pressed()
        # klahvi vajutusel liigub auto
        if pressed[pygame.K_LEFT]:
            autoX -= 4
            punane_auto = pygame.Rect(autoX, autoY, 45, 90)
        if pressed[pygame.K_RIGHT]:
            autoX += 4
            punane_auto = pygame.Rect(autoX, autoY, 45, 90)

        # kontrollib, kas punane auto on tee piirides ja piirab sisse
        if autoX < 150:
            autoX = 150
        if autoX > 450:
            autoX = 450

        # skoori kuvamine
        text = font.render(f"Skoor:{punktid}", True, [0,0,0]) # määrab teksti ja atribuudid
        screen.blit(text, [0,0]) # kuvab teksti ekraanil


    ### SINISE AUTODE KOOD ###

    # auto 1

        for auto in sinine_auto[:]:
            sinine_autoY += speedY # liigutab kordinaate alla vastavalt kiirusele
            auto.update(sinine_autoX, sinine_autoY, 45,90) # muudab auto positisooni
            if sinine_autoY > 480: # kui auto on alla jõudnud
                sinine_autoY = 0 # toob tagasi üles
                sinine_autoX = random.randint(150, 225) # määrab uue x kordinaadi
                speedY = random.randint(1, 2) # määrab uue kiiruse
                punktid += 1 # lisab punkti juurde

            # kui sinine auto läheb punasele pihta, siis on mäng läbi
            if punane_auto.colliderect(auto): 
                playing = False # katkestab mängu
        
        for auto in sinine_auto:
            screen.blit(sinine_auto_pilt, auto) # kuvab auto ekraanil

    # auto 2

        for auto2 in sinine_auto2[:]:
            sinine_autoY2 += speedY2 # liigutab kordinaate alla vastavalt kiirusele
            auto2.update(sinine_autoX2, sinine_autoY2, 45,90) # muudab auto positisooni
            if sinine_autoY2 > 480: # kui auto on alla jõudnud
                sinine_autoY2 = 0 # toob tagasi üles
                sinine_autoX2 = random.randint(275, 340) # määrab uue x kordinaadi
                speedY2 = random.randint(1, 2) # määrab uue kiiruse
                punktid += 1 # lisab punkti juurde

            # kui sinine auto läheb punasele pihta, siis on mäng läbi
            if punane_auto.colliderect(auto2): 
                playing = False # katkestab mängu
        
        for auto2 in sinine_auto2:
            screen.blit(sinine_auto_pilt2, auto2) # kuvab auto ekraanil

    # auto 3

        for auto3 in sinine_auto3[:]:
            sinine_autoY3 += speedY3 # liigutab kordinaate alla vastavalt kiirusele
            auto3.update(sinine_autoX3, sinine_autoY3, 45,90) # muudab auto positisooni
            if sinine_autoY3 > 480: # kui auto on alla jõudnud
                sinine_autoY3 = 0 # toob tagasi üles
                sinine_autoX3 = random.randint(375, 450) # määrab uue x kordinaadi
                speedY3 = random.randint(1, 2) # määrab uue kiiruse
                punktid += 1 # lisab punkti juurde

            # kui sinine auto läheb punasele pihta, siis on mäng läbi
            if punane_auto.colliderect(auto3): 
                playing = False # katkestab mängu
        
        for auto3 in sinine_auto3:
            screen.blit(sinine_auto_pilt3, auto3) # kuvab auto ekraanil

    pygame.display.flip()     #graafika kuvamine ekraanil
    screen.blit(taust,[0,0])     # tausta kuvamine
    screen.blit(punane_auto_pilt, punane_auto)     # punase auto kuvamine


pygame.quit()