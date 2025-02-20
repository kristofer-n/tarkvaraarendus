import pygame
pygame.init()
#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Harjutamine")
screen.fill([204, 255, 204])

#Lisame pildid
bg = pygame.image.load("harjutus2/Sissejuhatus/img/bg.png")
screen.blit(bg,[0,0])
youWin = pygame.image.load("harjutus2/Sissejuhatus/img/youwin.png")
youWin = pygame.transform.scale(youWin, [300, 120])
screen.blit(youWin,[180,100])

pygame.display.flip()
# akna lahtipüsimiseks vajalik
running = True
while running:

# for loop through the event queue

   for event in pygame.event.get():

       # Check for QUIT event

       if event.type == pygame.QUIT:

           running = False