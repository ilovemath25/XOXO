import pygame
from page.frame import frame
class Mainpage:
   button1     = [pygame.image.load('image/button/button_2v2.png'),pygame.image.load('image/button/button_2v2_glow.png'),]
   button2     = [pygame.image.load('image/button/button_vsai.png'),pygame.image.load('image/button/button_vsai_glow.png')]
   buttonframe = [pygame.image.load('image/button/button_frame1.png'),pygame.image.load('image/button/button_frame2.png'),
                  pygame.image.load('image/button/button_frame3.png'),pygame.image.load('image/button/button_frame4.png')]
   def __init__(self):
      self.choice1 = True
      self.animate1 = False
      self.choice2 = False
      self.animate2 = False
      self.confirm = False
      self.countanimate = 0
   def reset(self):
      self.choice1 = True
      self.animate1 = False
      self.choice2 = False
      self.animate2 = False
      self.confirm = False
      self.countanimate = 0
   def draw(self,win):
      frame(win)
      win.blit(pygame.image.load('image/title.png'),(50,10))
      if self.animate1:
         pygame.time.delay(40)
         if self.countanimate<4:win.blit(self.buttonframe[self.countanimate],(50,360))
         else:
            self.animate1 = False
            self.countanimate = 0
         self.countanimate+=1
      else:
         if not self.choice1:win.blit(self.button1[0],(50,360))
         elif self.choice1:win.blit(self.button1[1],(50,360))
      if self.animate2:
         pygame.time.delay(40)
         if self.countanimate<4:win.blit(self.buttonframe[self.countanimate],(330,360))
         else:
            self.animate2 = False
            self.countanimate = 0
         self.countanimate+=1
      else:
         if not self.choice2:win.blit(self.button2[0],(330,360))
         elif self.choice2:win.blit(self.button2[1],(330,360))
   def key(self,keys):
      if not self.animate1 and not self.animate2:
         if (keys[pygame.K_LEFT] or keys[pygame.K_a]):
            if not self.choice1:self.animate1 = True
            self.choice1 = True
            self.choice2 = False
         elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
            if not self.choice2:self.animate2 = True
            self.choice1 = False
            self.choice2 = True