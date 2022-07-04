
import pygame

from Token import *


class Square(Token):
  '''
  Represents a class that shows just a 2x2 square
  Reference point for drawing is the upper left corner
  '''
  
  def __init__(self, x,y, width, height) -> None:
    super().__init__(x,y,width,height)
    self.color=color_constants.CYAN2

    # Add a better handle for the single rect which represents this class
    # This is easier than using self.rects[0] all the time
    self.rect = pygame.Rect(x, y, width, height)
    self.rects.append(self.rect)

  def rotate(self, degree):
    pass

  

  def move(self, vx, vy):
    if self.is_movable():
      super().move_after_check(vx, vy)


  



