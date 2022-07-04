
import pygame

from Token import *


class Square(Token):
  '''
  Represents a class that shows just a 2x2 square
  Reference point for drawing is the upper left corner
  '''
  
  def __init__(self, x,y, width, height) -> None:
    super().__init__(x,y,width,height)
    self.color=color_constants.BLUE2

    # Add a better handle for the single rect which represents this class
    # This is easier than using self.rects[0] all the time
    self.rect = pygame.Rect(x, y, width, height)
    self.rects.append(self.rect)

  def rotate(self, degree):
    pass


  def move(self, vx, vy, BORDER):
    if self.is_movable():
      if self.x + self.width + vx < BORDER.width and self.y + self.height < BORDER.height:
        super().move_after_check(vx, vy)

  def collides_with_single_square(self, other_square):
    collision_detected=False
    if self != other_square:
      for me_part_rect in self.rects:
        for other_part_rect in other_square.rects:
          if me_part_rect.colliderect(other_part_rect):
            collision_detected=True
            break
    return collision_detected

  def collides_with_multiple_squares(self, other_squares):
    for other_square in other_squares:
      if self.collides_with_single_square(other_square=other_square):
        return True




