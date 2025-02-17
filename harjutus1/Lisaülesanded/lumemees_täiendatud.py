# Kristofer Nagaicevs IS24 17.02.25

import pygame # importib pygame

# initialiseerib pygame
pygame.init()

# määrab ekraani parameetrid
screen=pygame.display.set_mode([300,300])
pygame.display.set_caption("Lumemees - Kristofer Nagaicevs")

# täidab ekraani helesinise värviga
screen.fill([100, 200, 250])

# joonistab valged ringid (keha)
pygame.draw.circle(screen, [255, 255, 255], [150,225], 50, 50)
pygame.draw.circle(screen, [255, 255, 255], [150,140], 40, 40)
pygame.draw.circle(screen, [255, 255, 255], [150,75], 30, 30)

# joonistab mustab ringid (silmad)
pygame.draw.circle(screen, [0, 0, 0], [140,70], 5, 5)
pygame.draw.circle(screen, [0, 0, 0], [160,70], 5, 5)

# joonistab kolmnurga (nina)
pygame.draw.polygon(screen, [255, 0, 0], [[145,80],[155,80],[150,95]], 0)

# joonistab mustab ringid (nööbid)
pygame.draw.circle(screen, [0, 0, 0], [150,120], 5, 5)
pygame.draw.circle(screen, [0, 0, 0], [150,140], 5, 5)
pygame.draw.circle(screen, [0, 0, 0], [150,160], 5, 5)

# joonistab kübara
pygame.draw.rect(screen, [20, 20, 20], [130, 10, 40, 30], 0)
pygame.draw.rect(screen, [20, 20, 20], [120, 40, 60, 10], 0)
pygame.draw.rect(screen, [255, 255, 255], [130, 35, 40, 5], 0)

# joonistab käed
pygame.draw.line(screen, [100,60,40], [120,120], [50,200], 10)
pygame.draw.line(screen, [100,60,40], [180,120], [250,200], 10)

# joonistab päike
pygame.draw.circle(screen, [255, 255, 0], [250,50], 20, 0)

pygame.draw.line(screen, [255,255,0], [250,50], [250,90], 3)
pygame.draw.line(screen, [255,255,0], [250,50], [290,50], 3)
pygame.draw.line(screen, [255,255,0], [250,50], [250,10], 3)
pygame.draw.line(screen, [255,255,0], [250,50], [210,50], 3)

# joonistab pilved
pygame.draw.ellipse(screen, [255, 255, 255], [30, 50, 70, 30], 0)
pygame.draw.ellipse(screen, [255, 255, 255], [200, 90, 70, 30], 0)
pygame.draw.ellipse(screen, [255, 255, 255], [20, 120, 70, 30], 0)

# joonistab harja
pygame.draw.line(screen, [100,60,40], [50,70], [50,270], 10)
pygame.draw.line(screen, [100,60,40], [20,70], [80,70], 10)

pygame.draw.line(screen, [100,60,40], [25,70], [25,30], 5)
pygame.draw.line(screen, [100,60,40], [35,70], [35,30], 5)
pygame.draw.line(screen, [100,60,40], [45,70], [45,30], 5)
pygame.draw.line(screen, [100,60,40], [55,70], [55,30], 5)
pygame.draw.line(screen, [100,60,40], [65,70], [65,30], 5)
pygame.draw.line(screen, [100,60,40], [75,70], [75,30], 5)

# akna lahtipüsimiseks vajalik
pygame.display.flip()
running = True
while running:

# for loop through the event queue

   for event in pygame.event.get():

       # Check for QUIT event

       if event.type == pygame.QUIT:

           running = False