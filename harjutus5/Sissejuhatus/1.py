import pygame
pygame.init()
 
#värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]
 
#ekraani seaded
screenX = 640
screenY = 480
screen=pygame.display.set_mode([screenX,screenY])
pygame.display.set_caption("Surface")
screen.fill(lBlue)

#Surface kasutamine
surf = pygame.Surface((200,200))
pygame.draw.circle(surf,blue,(140,100), 100)
pygame.draw.circle(surf,green,(100,160), 80)
pygame.draw.circle(surf,pink,(50,100), 60)
screen.blit(surf,(0,0))

gameover = False
while not gameover:
    #mängu sulgemine ristist
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    pygame.display.flip()
pygame.quit()