import pygame
from page.main_page import Mainpage
from page.v2v2_page import V2v2
from page.vsai_page import Vsai
from page.loading import Loading
from page.windraw import Windraw
pygame.init()
in_main_page = True
in_2v2 = False
in_vsai = False
in_choose = False
in_won = False
in_draw = False
win = pygame.display.set_mode((600,550))
mainpage = Mainpage()
v2v2 = V2v2()
vsai = Vsai()
loading = Loading()
windraw = Windraw()
run = True
xwon = False
owon = False
gamedraw = False
count=0
pygame.display.set_caption("xoxo")
def draw():
   if in_main_page:mainpage.draw(win)
   elif in_2v2:v2v2.draw(win)
   elif in_choose:vsai.choose(win)
   elif in_vsai:vsai.draw(win)
   elif in_won or in_draw:windraw.draw(win,xwon,owon,gamedraw)
   pygame.display.update()
while run:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:run = False
   draw()
   keys = pygame.key.get_pressed()
   if in_main_page:
      mainpage.key(keys)
      if(keys[pygame.K_RETURN]):
         in_main_page = False
         loading.reset()
         loading.loadx(win,3)
         if mainpage.choice1:in_2v2 = True
         elif mainpage.choice2:in_choose = True
   elif in_2v2:
      v2v2.key()
      run = v2v2.runv2v2
      xwon,owon,gamedraw = v2v2.won()
      if xwon or owon:
         in_won=True
         in_2v2=False
         pygame.time.delay(1000)
      elif gamedraw:
         in_draw=True
         in_2v2=False
         pygame.time.delay(1000)
   elif in_vsai:
      vsai.key()
      run = vsai.runvsai
      xwon,owon,gamedraw = vsai.won()
      if xwon or owon:
         in_won=True
         in_vsai=False
         pygame.time.delay(1000)
      elif gamedraw:
         in_draw=True
         in_vsai=False
         pygame.time.delay(1000)
   elif in_choose:
      vsai.choosekey()
      run = vsai.runvsai
      count+=1
      if(keys[pygame.K_RETURN]) and count>10:
         loading.reset()
         loading.loadx(win,3)
         in_choose = False
         in_vsai = True
         count=0
   elif in_won or in_draw:
      windraw.key()
      run = windraw.run
      if(keys[pygame.K_RETURN]):
         in_won = False
         in_draw = False
         owon = False
         xwon = False
         gamedraw = False
         loading.reset()
         loading.loadx(win,3)
         if windraw.choice1:
            pygame.display.update()
            v2v2.reset()
            vsai.reset(False)
            if mainpage.choice1:in_2v2 = True
            elif mainpage.choice2:in_vsai = True
         elif windraw.choice2:
            pygame.display.update()
            in_main_page = True
            mainpage.reset()
            v2v2.reset()
            vsai.reset(True)
   pygame.display.update()
   #print(keys[pygame.K_RETURN])
pygame.quit()