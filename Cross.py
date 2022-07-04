
import color_constants
import pygame
from Token import *


class Cross(Token):
  '''
  Represents a class that shows a cross
    x  
  x x x
    x
  Reference point for drawing is the upper left of the cross
  '''
  
  def __init__(self, x,y, width, height) -> None:
    super().__init__(x,y,width,height)
    self.color=color_constants.BLUE2

    # Create the 3 rectangles that reprensent the cross
    self.rects.append(pygame.Rect(x + width//3, y, width//3, height//3))
    self.rects.append(pygame.Rect(x, y + height//3, width, height//3))
    self.rects.append(pygame.Rect(x+width//3, y+2*height//3, width//3, height//3))

  def rotate(self, degree):
    pass


  def move(self, vx, vy, BORDER):
    if self.is_movable():
      if self.x + self.width + vx < BORDER.width and self.y + self.height < BORDER.height:
        super().move_after_check(vx, vy)
