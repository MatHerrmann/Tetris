
import color_constants
import random
import pygame

from main import HEIGHT, WIDTH

class Square():
  '''
  Represents a class that shows just a 2x2 square
  Reference point for drawing is the upper left corner
  '''
  # COLOR=random.choice(list(color_constants.colors))
  COLOR=color_constants.BLUE2

  
  def __init__(self, x,y, WIDTH, HEIGHT) -> None:
    self.rect=pygame.Rect(x, y, WIDTH, HEIGHT)    
    self.movable=True

  def rotate(self, degree):
    pass

  def draw(self, screen):
    pygame.draw.rect(screen, self.COLOR, self.rect,0)

  def is_movable(self):    
    return self.movable

  def set_movable(self, new_value):
    self.movable=new_value


  def move(self, vx, vy, BORDER):
    if self.is_movable():
      if self.rect.x + self.rect.width + vx < BORDER.width and self.rect.y + self.rect.height < BORDER.height:
        self.rect.x += vx
        self.rect.y += vy

  def collides_with_single_square(self, other_square):
    if self != other_square:
    # print(f'Me {self.rect}, other {other_square.rect}')
      return self.rect.colliderect(other_square.rect)
    else:
      False

  def collides_with_multiple_squares(self, other_squares):
    for other_square in other_squares:
      if self.collides_with_single_square(other_square=other_square):
        return True

  def is_out_of_screen(self, screen):
    if self.rect.x > screen.get_width() or self.rect.y > screen.get_height():
      return True
    else:
      return False




