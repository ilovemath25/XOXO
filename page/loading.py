import pygame
from page.frame import frame
class Loading:
   def __init__(self):
      self.load_count = 0
   def reset(self):
      self.load_count = 0
   def loadx(self,win,delay):
      while self.load_count<61:
         pygame.time.delay(delay)
         frame(win)
         win.blit(pygame.image.load('image/title.png'),(50,10))
         win.blit(pygame.font.SysFont('dejavusansmono',20,True).render('Loading...',1,(255,255,0)),(230,420))
         #pygame.draw.rect(win,(100,100,100),(90,380,420,25), border_radius=10)
         pygame.draw.rect(win,(255,255,0),(90,380,7*self.load_count,25), border_radius=10)
         win.blit(pygame.transform.smoothscale(pygame.image.load('image/loading_bar.png'),(512,400)),(38,96))
         self.load_count+=1
         pygame.display.update()