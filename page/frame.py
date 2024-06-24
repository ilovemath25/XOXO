import pygame
def frame(win):
   pygame.draw.rect(win,(0,0,0),(0,0,600,600))
   win.blit(pygame.image.load('image/bg.jpg'),(0,0))
   pygame.draw.rect(win,(0,205,0),(0,0,600,15))
   pygame.draw.rect(win,(0,205,0),(0,535,600,15))
   pygame.draw.rect(win,(0,205,0),(0,0,15,550))
   pygame.draw.rect(win,(0,205,0),(585,0,15,550))
   pygame.draw.rect(win,(255,255,255),(5,5,590,5))
   pygame.draw.rect(win,(255,255,255),(5,540,590,5))
   pygame.draw.rect(win,(255,255,255),(5,5,5,535))
   pygame.draw.rect(win,(255,255,255),(590,5,5,535))