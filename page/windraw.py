import pygame
from page.frame import frame
class Windraw():
   button1     = [pygame.image.load('image/button/retry.png'),pygame.image.load('image/button/retry_glow.png'),]
   button2     = [pygame.image.load('image/button/back.png'),pygame.image.load('image/button/back_glow.png')]
   buttonframe = [pygame.image.load('image/button/button_frame1.png'),pygame.image.load('image/button/button_frame2.png'),
                  pygame.image.load('image/button/button_frame3.png'),pygame.image.load('image/button/button_frame4.png')]
   def __init__(self):
      self.choice1 = True
      self.animate1 = False
      self.choice2 = False
      self.animate2 = False
      self.confirm = False
      self.countanimate = 0
      self.run = True
   def reset(self):
      self.choice1 = True
      self.animate1 = False
      self.choice2 = False
      self.animate2 = False
      self.confirm = False
      self.countanimate = 0
      self.run = True
   def draw(self,win,xwon,owon,gamedraw):
      frame(win)
      if xwon:
         win.blit(pygame.image.load('image/x_symbol.png'),(100,200))
         win.blit(pygame.image.load('image/won.png'),(20,10))
      elif owon:
         win.blit(pygame.image.load('image/o_symbol.png'),(100,200))
         win.blit(pygame.image.load('image/won.png'),(20,10))
      elif gamedraw:
         win.blit(pygame.image.load('image/draw.png'),(0,0))
      if self.animate1:
         pygame.time.delay(40)
         if self.countanimate<4:win.blit(self.buttonframe[self.countanimate],(10,420))
         else:
            self.animate1 = False
            self.countanimate = 0
         self.countanimate+=1
      else:
         if not self.choice1:win.blit(self.button1[0],(10,420))
         elif self.choice1:win.blit(self.button1[1],(10,420))
      if self.animate2:
         pygame.time.delay(40)
         if self.countanimate<4:win.blit(self.buttonframe[self.countanimate],(370,420))
         else:
            self.animate2 = False
            self.countanimate = 0
         self.countanimate+=1
      else:
         if not self.choice2:win.blit(self.button2[0],(370,420))
         elif self.choice2:win.blit(self.button2[1],(370,420))
   def key(self):
      for event in pygame.event.get():
         if event.type == pygame.QUIT:self.run = False
         elif event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_RIGHT)or(event.key == pygame.K_a):
               if not self.choice1:self.animate1 = True
               self.choice1 = True
               self.choice2 = False
            elif(event.key == pygame.K_LEFT)or(event.key == pygame.K_d):
               if not self.choice2:self.animate2 = True
               self.choice1 = False
               self.choice2 = True