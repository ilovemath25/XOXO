import pygame
from page.frame import frame
cord_box = (
   [19,25 ],[142,25 ],[265,25 ],
   [19,138],[142,138],[265,138],
   [19,251],[142,251],[265,251],
)
class V2v2:
   def __init__(self):
      self.xo_put = {}
      self.select_x = 19
      self.select_y = 25
      self.runv2v2 = True
      self.move = 123
      self.put = False
      self.turn = 1
      self.symbol = 'x' if self.turn else 'o'
      self.x_won = False
      self.o_won = False
      self.game_draw = False
   def reset(self):
      self.xo_put = {}
      self.select_x = 19
      self.select_y = 25
      self.runv2v2 = True
      self.move = 123
      self.put = False
      self.turn = 1
      self.symbol = 'x' if self.turn else 'o'
      self.x_won = False
      self.o_won = False
      self.game_draw = False
   def putxo(self,win,xoro):
      win.blit(pygame.image.load('image/'+xoro+'_symbol.png'),(self.select_x,self.select_y))
      if (xoro not in self.xo_put):self.xo_put[xoro]=[[self.select_x,self.select_y]]
      else:self.xo_put[xoro].append([self.select_x,self.select_y])
      self.put = False
      self.turn = not self.turn
   def draw(self,win):
      frame(win)
      win.blit(pygame.image.load('image/game_frame.png'),(0,0))
      win.blit(pygame.image.load('image/selected_box.png'),(self.select_x,self.select_y))
      win.blit(pygame.transform.smoothscale(pygame.image.load('image/'+self.symbol+'_symbol.png'),(123,123)),(440,25))
      self.symbol = 'x' if self.turn else 'o'
      win.blit(pygame.font.SysFont('dejavusansmono',22,True).render('TURN',1,(255,255,255)),(475,130))
      for xo,cord in self.xo_put.items():
         if xo=='x':
            for xy in cord:win.blit(pygame.image.load('image/x_symbol.png'),(xy[0],xy[1]))
         elif xo=='o':
            for xy in cord:win.blit(pygame.image.load('image/o_symbol.png'),(xy[0],xy[1]))
      for xo,cord in self.xo_put.items():
         for xy in cord:
            if[self.select_x,self.select_y]==xy:self.put=False
      if(self.put):
         if self.turn:self.putxo(win,'x')
         else:self.putxo(win,'o')
   def checkwon(self,cord):
      if cord_box[0] in cord and cord_box[1] in cord and cord_box[2] in cord:return True
      elif cord_box[3] in cord and cord_box[4] in cord and cord_box[5] in cord:return True
      elif cord_box[6] in cord and cord_box[7] in cord and cord_box[8] in cord:return True
      elif cord_box[0] in cord and cord_box[3] in cord and cord_box[6] in cord:return True
      elif cord_box[1] in cord and cord_box[4] in cord and cord_box[7] in cord:return True
      elif cord_box[2] in cord and cord_box[5] in cord and cord_box[8] in cord:return True
      elif cord_box[0] in cord and cord_box[4] in cord and cord_box[8] in cord:return True
      elif cord_box[2] in cord and cord_box[4] in cord and cord_box[6] in cord:return True
      return False
   def won(self):
      for xo,cord in self.xo_put.items():
         if xo=='x':self.x_won=self.checkwon(cord)
         elif xo=='o':self.o_won=self.checkwon(cord)
      if 'o' in self.xo_put and 'x' in self.xo_put:
         if len(self.xo_put['x']+self.xo_put['o'])==9:self.game_draw=True
      return self.x_won,self.o_won,self.game_draw
   def key(self):
      for event in pygame.event.get():
         if event.type == pygame.QUIT:self.runv2v2 = False
         elif event.type == pygame.KEYDOWN:
            if((event.key == pygame.K_LEFT)or(event.key == pygame.K_a))and(self.select_x>19):self.select_x-=self.move
            elif((event.key == pygame.K_RIGHT)or(event.key == pygame.K_d)and(self.select_x<200)):self.select_x+=self.move
            elif((event.key == pygame.K_UP)or(event.key == pygame.K_w)and(self.select_y>25)):self.select_y-=self.move-10
            elif((event.key == pygame.K_DOWN)or(event.key == pygame.K_s)and(self.select_y<200)):self.select_y+=self.move-10
            elif(event.key == pygame.K_RETURN):self.put=True