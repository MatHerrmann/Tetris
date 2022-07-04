import pygame
import random
import color_constants
from Square import *
from Cross import *

WIDTH, HEIGHT = 500,800
BOX_WIDTH, BOX_HEIGHT = 50,50
FPS=60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BORDER = pygame.Rect(0,0, WIDTH, HEIGHT)
TICK_EVENT = pygame.USEREVENT + 1


pygame.display.set_caption('Tetris')

def move_objects(active_objects):
  for object in active_objects:
    object.move(0, BOX_HEIGHT, BORDER)    
    if object.collides_with_multiple_tokens(active_objects):
      object.move(0, -BOX_HEIGHT, BORDER)
      object.set_movable(False)


def check_in_screen(screen, active_objects):
  out_of_screen_objects=list()
  for object in active_objects:
    if object.is_out_of_screen(screen):
      out_of_screen_objects.append(object)
  return out_of_screen_objects

def draw_window(active_objects):
  WIN.fill(color_constants.WHITE)
  for object in active_objects:
    object.draw(WIN)
  for x in range(0, WIDTH, BOX_WIDTH):
    for y in range(0, HEIGHT, BOX_HEIGHT):
      rect = pygame.Rect(x, y, BOX_WIDTH, BOX_HEIGHT)
      pygame.draw.rect(WIN, color_constants.BLACK, rect,1)
  pygame.display.update()

def spawn_square(active_objects):
  nr_boxes_width, nr_boxes_height=2,2
  found=False
  while not found:
    x = random.randrange(0, WIDTH-nr_boxes_width*BOX_WIDTH, nr_boxes_width*BOX_WIDTH)
    y = 0
    square = Square(x,y, nr_boxes_height*BOX_HEIGHT, nr_boxes_width*BOX_WIDTH)
    if not square.collides_with_multiple_tokens(active_objects):
      found=True
  return square

def spawn_cross(active_objects):
  nr_boxes_width, nr_boxes_height=3,3
  found=False
  while not found:
    x = random.randrange(0, WIDTH-nr_boxes_width*BOX_WIDTH, nr_boxes_width*BOX_WIDTH)
    y = 0
    cross = Cross(x,y, nr_boxes_height*BOX_HEIGHT, nr_boxes_width*BOX_WIDTH)
    if not cross.collides_with_multiple_tokens(active_objects):
      found=True
  return cross

def main():
  clock = pygame.time.Clock()
  pygame.time.set_timer(TICK_EVENT, 1000)
  tick_counter=0
  spawn_frequency=5
  test_spawn_objects=5
  running = True
  active_objects=list()
  while running:
    clock.tick(FPS)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      if event.type == TICK_EVENT:
        tick_counter += 1
        print(f'Tick {tick_counter}')
        move_objects(active_objects)
        if tick_counter % spawn_frequency:
          if len(active_objects) < test_spawn_objects:
            new_square=spawn_cross(active_objects)
            active_objects.append(new_square)
    
    draw_window(active_objects)
  pygame.quit()


if __name__ == '__main__':
    main()

  
