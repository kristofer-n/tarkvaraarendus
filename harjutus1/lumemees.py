# Kristofer Nagaicevs IS24 17.02.25

import pygame # importib pygame

# initialiseerib pygame
pygame.init()

# määrab ekraani parameetrid
screen=pygame.display.set_mode([300,300])
pygame.display.set_caption("Lumemees - Kristofer Nagaicevs")

# täidab ekraani musta värviga
screen.fill([0, 0, 0])

# joonistab valged ringid (keha)
pygame.draw.circle(screen, [255, 255, 255], [150,225], 50, 50)
pygame.draw.circle(screen, [255, 255, 255], [150,140], 40, 40)
pygame.draw.circle(screen, [255, 255, 255], [150,75], 30, 30)

# joonistab mustab ringid (silmad)
pygame.draw.circle(screen, [0, 0, 0], [140,70], 5, 5)
pygame.draw.circle(screen, [0, 0, 0], [160,70], 5, 5)

# joonistab kolmnurga (nina)
pygame.draw.polygon(screen, [255, 0, 0], [[145,80],[155,80],[150,95]], 0)

# akna lahtipüsimiseks vajalik
pygame.display.flip()
running = True
while running:

# for loop through the event queue

   for event in pygame.event.get():

       # Check for QUIT event

       if event.type == pygame.QUIT:

           running = False