
import color_constants
import pygame
from Token import *


class Stick(Token):
  '''
  Represents a class that shows a stick
  x  
  x
  x
  Reference point for drawing is the upper left of the stick
  Rotation point is also the upper left corner of the stick
  '''
  
  def __init__(self, x,y, width, height) -> None:
    super().__init__(x,y,width,height)
    self.color=color_constants.GREEN

    # Create the 3 rectangles that reprensent the cross
    self.rects.append(pygame.Rect(x, y, width, height))

  def rotate(self, degree):
    if degree == 90 or degree == -270 or degree == 90 or degree == 270:
      tmp_height = self.rects[0].height
      self.rects[0].height = self.rects[0].width
      self.height = self.width
      self.rects[0].width = tmp_height
      self.width = tmp_height



  def move(self, vx, vy):
    if self.is_movable():
      super().move_after_check(vx, vy)
