from Stick import *
from Square import *
from Cross import *
import random

class TokenGenerator():
  def __init__(self, box_width, box_height, width) -> None:
    random.seed()
    self.box_width=box_width
    self.box_height=box_height
    self.screen_width=width

  def spawn_token(self):
    function_list = [ self._spawn_cross, self._spawn_square, self._spawn_stick ]
    return random.choice(function_list)()

  def _spawn_square(self):
    nr_boxes_width, nr_boxes_height=2,2
    x = random.randrange(0, self.screen_width-nr_boxes_width*self.box_width, nr_boxes_width*self.box_width)
    y = 0
    square = Square(x,y, nr_boxes_height*self.box_height, nr_boxes_width*self.box_width)
    return square

  def _spawn_cross(self):
    nr_boxes_width, nr_boxes_height=3,3
    x = random.randrange(0, self.screen_width-nr_boxes_width*self.box_width, self.box_width)
    y = 0
    cross = Cross(x,y, nr_boxes_height*self.box_height, nr_boxes_width*self.box_width)
    return cross

  def _spawn_stick(self):
    nr_boxes_width, nr_boxes_height=6,1
    x = random.randrange(0, self.screen_width-nr_boxes_width*self.box_width, self.box_width)
    y = 0
    stick = Stick(x,y, nr_boxes_height*self.box_height, nr_boxes_width*self.box_width)
    return stick
