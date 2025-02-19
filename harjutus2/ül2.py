# Kristofer Nagaicevs IS24 19.02.25

import pygame # importib pygame

# initialiseerib pygame
pygame.init()

# määrab ekraani parameetrid
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Ülesanne 2")

# täidab ekraani musta värviga
screen.fill([0, 0, 0])

# lisab taustapildi
bg = pygame.image.load("harjutus2/img/bg_shop.jpg")
screen.blit(bg,[0,0])

# lisab müüja
seller = pygame.image.load("harjutus2/img/seller.png")
seller = pygame.transform.scale(seller, [255, 305])
screen.blit(seller,[105,158])

# lisab jutumulli
chat = pygame.image.load("harjutus2/img/chat.png")
chat = pygame.transform.scale(chat, [257, 210])
screen.blit(chat,[245,60])

# lisab teksti
font = pygame.font.Font(pygame.font.match_font('sansserif'), 23)
text = font.render("Tere, olen Kristofer Nagaicevs", True, [100,100,255])

# tekstikasti suurus
text_width = text.get_rect().width
text_height = text.get_rect().height

# paneb teksti ekraanile, määrab suuruse
screen.blit(text, [260,150])

# akna lahtipüsimiseks vajalik
pygame.display.flip()
running = True
while running:

# for loop through the event queue

   for event in pygame.event.get():

       # Check for QUIT event

       if event.type == pygame.QUIT:

           running = False