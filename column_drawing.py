import pygame

class visualization(object):
  def __init__(self, game, width, height):
    self.game=game
    self.window_width = width
    self.window_height = height
  
  def tick(self):
    pass
  
  def draw(self, drawList, markedItem):
    self.grid = self.window_width/(len(drawList)+2)
    self.position = 1
    maxValue = max(drawList)
    if maxValue > 0:
      for item in drawList:
        scaled_item = int(item * (self.window_height/maxValue)) * (-1)
        rect = pygame.Rect((self.position*self.grid, self.window_height),(self.grid, scaled_item ))
        if self.position == markedItem:
          pygame.draw.rect(self.game.screen,(150,150,255),rect)
        else:
          pygame.draw.rect(self.game.screen,(0,150,255),rect)
        self.position += 1
