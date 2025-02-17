# Kristofer Nagaicevs IS24 17.02.25

import pygame # importib pygame

# initialiseerib pygame
pygame.init()

# määrab ekraani parameetrid
screen=pygame.display.set_mode([300,300])
pygame.display.set_caption("Lumemees - Kristofer Nagaicevs")

# täidab ekraani musta värviga
screen.fill([0, 0, 0])

# joonistab ristküliku
pygame.draw.rect(screen, [128, 128, 128], [100, 10, 100, 270], 2)

# joonistab ringid
pygame.draw.circle(screen, [255, 0, 0], [150,60], 40, 0)
pygame.draw.circle(screen, [255, 255, 0], [150,145], 40, 0)
pygame.draw.circle(screen, [0, 255, 0], [150,230], 40, 0)

# akna lahtipüsimiseks vajalik
pygame.display.flip()
running = True
while running:

# for loop through the event queue

   for event in pygame.event.get():

       # Check for QUIT event

       if event.type == pygame.QUIT:

           running = False