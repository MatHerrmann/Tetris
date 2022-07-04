import color_constants
import pygame

class Token():
  def __init__(self,x,y,width, height) -> None:
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.movable=True
    self.color = None
    self.rects = list()

  def is_movable(self):
    return self.movable

  def set_movable(self, movable):
    self.movable=movable

  def draw(self, screen):
    for part_rect in self.rects:
      pygame.draw.rect(screen, self.color, part_rect,0)

  def move_after_check(self, vx, vy):
    self.x += vx
    self.y += vy
    for part_rect in self.rects:
      part_rect.x += vx
      part_rect.y += vy

  def collides_with_single_token(self, other_token):
    collision_detected=False
    if self != other_token:
      for me_part_rect in self.rects:
        for other_part_rect in other_token.rects:
          if me_part_rect.colliderect(other_part_rect):
            collision_detected=True
            break
    return collision_detected

  def collides_with_multiple_tokens(self, other_tokens):
    for other_token in other_tokens:
      if self.collides_with_single_token(other_token):
        return True


  

  