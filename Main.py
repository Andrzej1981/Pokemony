import pygame as pg
import sys
from settings import *
from Container import *
import os


#http://clipart-library.com/clip-art/transparent-pokemon-21.htm - strona z pokemonami

path = os.getcwd()
path = path + "\Pikachu v1.0\img\\"
files = os.listdir(path)

paths = []
tabela = []
tabela1 = []

for s in files:
    paths.append(path+s)

for i in paths:
    tabela.append(pg.image.load(i))

class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.i=0
        self.new_game()
        self.tablica = []

    def new_game(self):
        pass

    def update(self):
        
       
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps():.1f}')

    def draw(self):
        self.screen.fill('black')
  
        for a in self.tablica:
            self.screen.blit(pg.transform.scale(tabela[a.obraz],(150,220)),a.pos)
        pikaczu = tabela[self.i]
        pikaczu = pg.transform.scale(pikaczu,(150,220))

        
        
        self.screen.blit(pikaczu,pg.mouse.get_pos())
        
        #self.map.draw()
        #self.player.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                left, middle, rigth = pg.mouse.get_pressed()
                if rigth:
                    self.i=self.i+1
                    if(self.i>=len(tabela)):
                        self.i=0      
                if left:
                    c=Container(self.i,pg.mouse.get_pos())
                    self.tablica.append(c)

                

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()
