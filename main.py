import pygame, sys
from column_drawing import visualization
import random
from bubble_sort import bubble_sort

class Game(object):
  def __init__(self):
    #Config
    self.max_tps = 1000.0
    self.window_height = 700
    self.window_width = 1280 

    #Initialization
    pygame.init()
    self.screen = pygame.display.set_mode((self.window_width,self.window_height))
    self.tps_clock = pygame.time.Clock()
    self.tps_delta = 0.0
    self.columns = visualization(self, self.window_width, self.window_height)
    self.sortingList = [0]
    self.sortingList = self.generateRandomList(0, self.window_height, int((self.window_width-2)/8))
    #self.sortingList = self.generateRandomList(0,10,5)
    self.actualiSortingIndex = 0
    self.columns.draw(self.sortingList, self.actualiSortingIndex)
    #inicjalizacja sortowania
    self.sorting = True
    self.sortingMethod = bubble_sort()

    while(True):
      #Events
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit(0)

      #Ticking
      self.tps_delta += self.tps_clock.tick()/1000.0
      while self.tps_delta > 1/self.max_tps:
        self.tick()
        self.tps_delta -= 1/self.max_tps

      #Drawing
      self.screen.fill((0,0,0))
      self.draw()
      pygame.display.update()
      pygame.display.flip()

  
  def tick(self):
    self.columns.tick()
    (self.sortingList, self.sorting, self.actualiSortingIndex) = self.sortingMethod.sort(self.sortingList, self.sorting)
  
  def draw(self):
    #self.columns.draw(self.sortingList)
    self.columns.draw(self.sortingList, self.actualiSortingIndex)
    #(self.sortingList, self.sorting, self.actualiSortingIndex) = self.sortingMethod.sort(self.sortingList, self.sorting)
    
  
  def generateRandomList(self, minValue, maxalue, size):
    return [random.randint(minValue, maxalue) for iter in range(size)]

if __name__ == "__main__": #wykona sie tylko jak uruchomimy bezposrednio
  Game()