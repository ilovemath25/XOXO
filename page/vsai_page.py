import pygame
import random
from page.frame import frame
cord_box = (
   [19,25 ],[142,25 ],[265,25 ],
   [19,138],[142,138],[265,138],
   [19,251],[142,251],[265,251],
)
cord_put = [
   [cord_box[0],cord_box[1],cord_box[2]],
   [cord_box[3],cord_box[4],cord_box[5]],
   [cord_box[6],cord_box[7],cord_box[8]],
   [cord_box[0],cord_box[3],cord_box[6]],
   [cord_box[1],cord_box[4],cord_box[7]],
   [cord_box[2],cord_box[5],cord_box[8]],
   [cord_box[0],cord_box[4],cord_box[8]],
   [cord_box[2],cord_box[4],cord_box[6]],
]
class Vsai:
   button0     = [pygame.image.load('image/button/easy.png'),pygame.image.load('image/button/easy_glow.png'),]
   button1     = [pygame.image.load('image/button/medium.png'),pygame.image.load('image/button/medium_glow.png')]
   button2     = [pygame.image.load('image/button/asian.png'),pygame.image.load('image/button/asian_glow.png'),]
   buttonframe = [pygame.image.load('image/button/button_choose_frame1.png'),pygame.image.load('image/button/button_choose_frame2.png'),
                  pygame.image.load('image/button/button_choose_frame3.png'),pygame.image.load('image/button/button_choose_frame4.png')]
   def __init__(self):
      self.xo_put = {}
      self.select_x = 19; self.select_y = 25; self.move = 123
      self.runvsai = True
      self.countanimate = self.difficulty = 0
      self.difanimate0 = self.difanimate1 = self.difanimate2 = False
      self.put = False
      self.turn = random.randint(0,1)
      self.symbol = 'x' if self.turn else 'o'
      self.ai = 'x' if self.symbol=='o' else 'o'
      self.turnsym = 'x'
      self.stage = 0
      self.first = self.turn
      self.x_won = self.o_won = self.game_draw = False
   def reset(self,difreset):
      self.xo_put = {}
      self.select_x = 19; self.select_y = 25; self.move = 123
      self.runvsai = True
      self.countanimate = 0
      if difreset:self.difficulty = 0
      self.difanimate0 = self.difanimate1 = self.difanimate2 = False
      self.put = False
      self.turn = random.randint(0,1)
      self.symbol = 'x' if self.turn else 'o'
      self.ai = 'x' if self.symbol=='o' else 'o'
      self.turnsym = 'x'
      self.stage = 0
      self.first = self.turn
      self.x_won = self.o_won = self.game_draw = False
   def putxo(self,win,xoro):
      win.blit(pygame.image.load('image/'+xoro+'_symbol.png'),(self.select_x,self.select_y))
      if (xoro not in self.xo_put):self.xo_put[xoro]=[[self.select_x,self.select_y]]
      else:self.xo_put[xoro].append([self.select_x,self.select_y])
      self.put = False
      self.turn = not self.turn
   def random_cord(self):
      cordx = cord_box[random.randint(0,8)]
      if 'x' in self.xo_put:
         while cordx in self.xo_put['x']:cordx = cord_box[random.randint(0,8)]
      if 'o' in self.xo_put:
         while cordx in self.xo_put['o']:cordx = cord_box[random.randint(0,8)]
      if 'o' in self.xo_put and 'x' in self.xo_put:
         while cordx in self.xo_put['x'] or cordx in self.xo_put['o']:cordx = cord_box[random.randint(0,8)]
      return cordx
   def result_in_xoput(self,list1,list2):
      #print('list',list1,list2)
      for row1 in list1:
         if row1 not in list2:return False
      return True
   def check_in_xo_put(self,result):
      result_list = []
      for subresult in result:
         #print(subresult,self.xo_put[self.symbol],self.result_in_xoput(subresult,self.xo_put[self.symbol]))
         if self.result_in_xoput(subresult,self.xo_put[self.symbol]):result_list.append(subresult)
      return result_list
   def xo_direction(self,xy):
      direction = [
         [xy[0],xy[1]-113],[xy[0],xy[1]+113],
         [xy[0]-123,xy[1]],[xy[0]+123,xy[1]],
         [xy[0]-123,xy[1]-113],[xy[0]+123,xy[1]+113],
         [xy[0]-123,xy[1]+113],[xy[0]+123,xy[1]-113],
      ]
      result = []
      for i in direction:
         if i[0]>18 and i[0]<270 and i[1]>24 and i[1]<270:result.append([[xy[0],xy[1]],i])
      return result
   def check_put(self,xy):
      result = self.xo_direction(xy)
      temp_list=[]
      result=self.check_in_xo_put(result)
      if result==None:return []
      for k in cord_put:
         for j in result:
            if self.result_in_xoput(j,k):
               temp_list = [element for element in k if element not in j][0]
               if 'x' in self.xo_put:
                  if temp_list in self.xo_put['x']:continue
               if 'o' in self.xo_put:
                  if temp_list in self.xo_put['o']:continue
               if 'o' in self.xo_put and 'x' in self.xo_put:
                  if temp_list in self.xo_put['x'] or temp_list in self.xo_put['o']:continue
               return temp_list
      return temp_list
   def block_opponent(self,xy1,xy2):
      for i in cord_put:
         if xy1 in i and xy2 in i:return [element for element in i if element not in [xy1,xy2]]
   def asian_level(self):
      if self.stage==0:
         if self.first==1:
            #print(cord_box[4],self.xo_put[self.symbol])
            if cord_box[4] not in self.xo_put[self.symbol]:return cord_box[4]
            else:return cord_box[6]
         else:return cord_box[6]
      elif self.stage==1:
         if self.first==1:
            temp = self.block_opponent(self.xo_put[self.symbol][0],self.xo_put[self.symbol][1])
            #print(temp,self.xo_put['x']+self.xo_put['o'])
            if temp!=None and temp[0] not in self.xo_put['x'] and temp[0] not in self.xo_put['o']:return temp[0]
            elif cord_box[6]in self.xo_put[self.ai] and cord_box[2]in self.xo_put[self.symbol] and cord_box[4]in self.xo_put[self.symbol]:return cord_box[8]
            elif cord_box[4]in self.xo_put[self.ai] and cord_box[1]in self.xo_put[self.symbol]:
               if cord_box[6]in self.xo_put[self.symbol] or cord_box[3]in self.xo_put[self.symbol]:return cord_box[0]
               elif cord_box[8]in self.xo_put[self.symbol] or cord_box[5]in self.xo_put[self.symbol]:return cord_box[2]
               elif cord_box[7]in self.xo_put[self.symbol]:return cord_box[0]
            elif cord_box[4]in self.xo_put[self.ai] and cord_box[3]in self.xo_put[self.symbol]:
               if cord_box[2]in self.xo_put[self.symbol] or cord_box[1]in self.xo_put[self.symbol]:return cord_box[0]
               elif cord_box[8]in self.xo_put[self.symbol] or cord_box[7]in self.xo_put[self.symbol]:return cord_box[6]
               elif cord_box[5]in self.xo_put[self.symbol]:return cord_box[0]
            elif cord_box[4]in self.xo_put[self.ai] and cord_box[5]in self.xo_put[self.symbol]:
               if cord_box[0]in self.xo_put[self.symbol] or cord_box[1]in self.xo_put[self.symbol]:return cord_box[2]
               elif cord_box[6]in self.xo_put[self.symbol] or cord_box[7]in self.xo_put[self.symbol]:return cord_box[8]
               elif cord_box[3]in self.xo_put[self.symbol]:return cord_box[0]
            elif cord_box[4]in self.xo_put[self.ai] and cord_box[7]in self.xo_put[self.symbol]:
               if cord_box[0]in self.xo_put[self.symbol] or cord_box[3]in self.xo_put[self.symbol]:return cord_box[6]
               elif cord_box[2]in self.xo_put[self.symbol] or cord_box[5]in self.xo_put[self.symbol]:return cord_box[8]
               elif cord_box[1]in self.xo_put[self.symbol]:return cord_box[0]
            else:
               temp = self.xo_direction([self.select_x,self.select_y])
               #print(temp,[self.select_x,self.select_y])
               for i in temp:
                  if i[1] not in self.xo_put['x']+self.xo_put['o']:return i[1]
         else:
            temp = [self.select_x,self.select_y]
            if temp==cord_box[4]:return cord_box[2]
            elif temp==cord_box[0] or temp==cord_box[1] or temp==cord_box[2] or temp==cord_box[3]:return cord_box[8]
            elif temp==cord_box[5] or temp==cord_box[7] or temp==cord_box[8]:return cord_box[0]
      elif self.stage==2:
         for i in self.xo_put[self.ai]:
            for j in self.xo_put[self.ai]:
               temp = self.block_opponent(i,j)
               if temp==None:temp=[];continue
               elif len(temp)>=2:temp=[];continue
               elif temp[0] in self.xo_put['x']+self.xo_put['o']:temp=[];continue
               else:
                  #print(temp)
                  return temp[0]
         for i in self.xo_put[self.symbol]:
            for j in self.xo_put[self.symbol]:
               temp = self.block_opponent(i,j)
               if temp==None:temp=[];continue
               elif len(temp)>=2:temp=[];continue
               elif temp[0] in self.xo_put['x']+self.xo_put['o']:temp=[];continue
               else:return temp[0]
         if self.first==1:return self.random_cord()
         else:
            if cord_box[6]in self.xo_put[self.ai] and cord_box[8]in self.xo_put[self.ai]:
               if cord_box[0]in self.xo_put[self.symbol] or cord_box[3]in self.xo_put[self.symbol]:return cord_box[2]
               elif cord_box[2]in self.xo_put[self.symbol]:return cord_box[0]
            elif cord_box[6]in self.xo_put[self.ai] and cord_box[0]in self.xo_put[self.ai]:
               if cord_box[7]in self.xo_put[self.symbol] or cord_box[8]in self.xo_put[self.symbol]:return cord_box[2]
      elif self.stage>=3:
         for i in self.xo_put[self.ai]:
            for j in self.xo_put[self.ai]:
               temp = self.block_opponent(i,j)
               if temp==None:temp=[];continue
               elif len(temp)>=2:temp=[];continue
               elif temp[0] in self.xo_put['x']+self.xo_put['o']:temp=[];continue
               else:
                  #print(temp)
                  return temp[0]
         for i in self.xo_put[self.symbol]:
            for j in self.xo_put[self.symbol]:
               temp = self.block_opponent(i,j)
               if temp==None:temp=[];continue
               elif len(temp)>=2:temp=[];continue
               elif temp[0] in self.xo_put['x']+self.xo_put['o']:temp=[];continue
               else:
                  #print(temp)
                  return temp[0]
         return self.random_cord()
   def putai_easy(self,win,xoro):
      pygame.time.delay(1000)
      cord = self.random_cord()
      win.blit(pygame.image.load('image/'+xoro+'_symbol.png'),(cord[0],cord[1]))
      if (xoro not in self.xo_put):self.xo_put[xoro]=[[cord[0],cord[1]]]
      else:self.xo_put[xoro].append([cord[0],cord[1]])
      self.put = False
      self.turn = not self.turn
   def putai_medium(self,win,xoro):
      pygame.time.delay(1000)
      list_cord = []
      cord = self.random_cord()
      if self.symbol in self.xo_put:
         for xy in self.xo_put[self.symbol]:list_cord.append(self.check_put(xy))
      for i in list_cord:
         if 'x' in self.xo_put:
            if i in self.xo_put['x']:continue
         if 'o' in self.xo_put:
            if i in self.xo_put['o']:continue
         if 'o' in self.xo_put and 'x' in self.xo_put:
            if i in self.xo_put['x'] or i in self.xo_put['o']:continue
         cord = i
      if cord==[]:cord = self.random_cord()
      win.blit(pygame.image.load('image/'+xoro+'_symbol.png'),(cord[0],cord[1]))
      if (xoro not in self.xo_put):self.xo_put[xoro]=[[cord[0],cord[1]]]
      else:self.xo_put[xoro].append([cord[0],cord[1]])
      self.put = False
      self.turn = not self.turn
   def putai_asian(self,win,xoro):
      pygame.time.delay(1000)
      cord = self.asian_level()
      #print(self.stage)
      win.blit(pygame.image.load('image/'+xoro+'_symbol.png'),(cord[0],cord[1]))
      if (xoro not in self.xo_put):self.xo_put[xoro]=[[cord[0],cord[1]]]
      else:self.xo_put[xoro].append([cord[0],cord[1]])
      self.put = False
      self.turn = not self.turn
      self.stage+=1
   def draw(self,win):  
      frame(win)
      win.blit(pygame.image.load('image/game_frame.png'),(0,0))
      win.blit(pygame.image.load('image/selected_box.png'),(self.select_x,self.select_y))
      for xo,cord in self.xo_put.items():
         if xo=='x':
            for xy in cord:win.blit(pygame.image.load('image/x_symbol.png'),(xy[0],xy[1]))
         elif xo=='o':
            for xy in cord:win.blit(pygame.image.load('image/o_symbol.png'),(xy[0],xy[1]))
      for xo,cord in self.xo_put.items():
         for xy in cord:
            if[self.select_x,self.select_y]==xy:self.put=False
      if self.turn:
         win.blit(pygame.transform.smoothscale(pygame.image.load('image/'+self.turnsym+'_symbol.png'),(123,123)),(440,25))
         win.blit(pygame.font.SysFont('dejavusansmono',22,True).render('YOUR TURN',1,(255,255,255)),(445,130))
         pygame.display.update()
         if(self.put):
            self.putxo(win,self.symbol)
            self.turnsym = 'x' if self.turnsym=='o' else 'o'
      else:
         win.blit(pygame.transform.smoothscale(pygame.image.load('image/'+self.turnsym+'_symbol.png'),(123,123)),(440,25))
         win.blit(pygame.font.SysFont('dejavusansmono',22,True).render('A.I. TURN',1,(255,255,255)),(445,130))
         pygame.display.update()
         if self.difficulty==0:self.putai_easy(win,self.ai)
         elif self.difficulty==1:self.putai_medium(win,self.ai)
         elif self.difficulty==2:self.putai_asian(win,self.ai)
         self.turnsym = 'x' if self.turnsym=='o' else 'o'
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
         if event.type == pygame.QUIT:self.runvsai = False
         elif event.type == pygame.KEYDOWN:
            if((event.key == pygame.K_LEFT)or(event.key == pygame.K_a))and(self.select_x>19):self.select_x-=self.move
            elif((event.key == pygame.K_RIGHT)or(event.key == pygame.K_d)and(self.select_x<200)):self.select_x+=self.move
            elif((event.key == pygame.K_UP)or(event.key == pygame.K_w)and(self.select_y>25)):self.select_y-=self.move-10
            elif((event.key == pygame.K_DOWN)or(event.key == pygame.K_s)and(self.select_y<200)):self.select_y+=self.move-10
            elif(event.key == pygame.K_RETURN):self.put=True
   def choose(self,win):
      frame(win)
      if self.difanimate0:
         pygame.time.delay(40)
         if self.countanimate<4:win.blit(self.buttonframe[self.countanimate],(185,181))
         else:
            self.difanimate0 = False
            self.countanimate = 0
         self.countanimate+=1
      else:
         if self.difficulty!=0:win.blit(self.button0[0],(185,181))
         elif self.difficulty==0:win.blit(self.button0[1],(185,181))
      if self.difanimate1:
         pygame.time.delay(40)
         if self.countanimate<4:win.blit(self.buttonframe[self.countanimate],(185,250))
         else:
            self.difanimate1 = False
            self.countanimate = 0
         self.countanimate+=1
      else:
         if self.difficulty!=1:win.blit(self.button1[0],(185,250))
         elif self.difficulty==1:win.blit(self.button1[1],(185,250))
      if self.difanimate2:
         pygame.time.delay(40)
         if self.countanimate<4:win.blit(self.buttonframe[self.countanimate],(185,319))
         else:
            self.difanimate2 = False
            self.countanimate = 0
         self.countanimate+=1
      else:
         if self.difficulty!=2:win.blit(self.button2[0],(185,319))
         elif self.difficulty==2:win.blit(self.button2[1],(185,319))
   def choosekey(self):
      for event in pygame.event.get():
         if event.type == pygame.QUIT:self.runvsai = False
         elif event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_UP)or(event.key == pygame.K_w):
               self.difficulty-=1
               if self.difficulty<0:self.difficulty+=3
               elif self.difficulty>2:self.difficulty-=3
               if self.difficulty==0:self.difanimate0 = True
               elif self.difficulty==1:self.difanimate1 = True
               elif self.difficulty==2:self.difanimate2 = True
            elif(event.key == pygame.K_DOWN)or(event.key == pygame.K_s):
               self.difficulty+=1
               if self.difficulty<0:self.difficulty+=3
               elif self.difficulty>2:self.difficulty-=3
               if self.difficulty==0:self.difanimate0 = True
               elif self.difficulty==1:self.difanimate1 = True
               elif self.difficulty==2:self.difanimate2 = True