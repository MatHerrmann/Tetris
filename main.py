import pygame
import random
import color_constants
from Square import *
from Cross import *
from TokenGenerator import *

WIDTH, HEIGHT = 500,800
BOX_WIDTH, BOX_HEIGHT = 20,20
FPS=60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BORDER = pygame.Rect(0,0, WIDTH, HEIGHT)
TICK_EVENT = pygame.USEREVENT + 1
SPAWN_EVENT = pygame.USEREVENT +2


pygame.display.set_caption('Tetris')

def move_token(moving_token, static_tokens):
    moving_token.move(0, BOX_HEIGHT)    
    if moving_token.collides_with_multiple_tokens(static_tokens) or moving_token.is_out_of_screen(BORDER):
      moving_token.move(0, -BOX_HEIGHT)
      moving_token.set_movable(False)
      static_tokens.append(moving_token)
      pygame.event.post(pygame.event.Event(SPAWN_EVENT))


def check_in_screen(screen, active_objects):
  out_of_screen_objects=list()
  for object in active_objects:
    if object.is_out_of_screen(screen):
      out_of_screen_objects.append(object)
  return out_of_screen_objects

def draw_window(moving_token, static_tokens):
  WIN.fill(color_constants.WHITE)
  moving_token.draw(WIN)
  for static_token in static_tokens:
    static_token.draw(WIN)
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

def spawn_cross():
  nr_boxes_width, nr_boxes_height=3,3
  x = random.randrange(0, WIDTH-nr_boxes_width*BOX_WIDTH, BOX_WIDTH)
  y = 0
  cross = Cross(x,y, nr_boxes_height*BOX_HEIGHT, nr_boxes_width*BOX_WIDTH)
  return cross

def main():
  clock = pygame.time.Clock()
  pygame.time.set_timer(TICK_EVENT, 100)
  tick_counter=0
  spawn_frequency=5
  test_spawn_objects=5
  running = True
  moving_token=None
  static_tokens=list()
  random.seed()
  pygame.event.post(pygame.event.Event(SPAWN_EVENT))
  token_gen = TokenGenerator(BOX_WIDTH, BOX_HEIGHT, WIDTH)
  while running:
    clock.tick(FPS)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      if event.type == TICK_EVENT:
        tick_counter += 1
        print(f'Tick {tick_counter}')
        if moving_token:
          move_token(moving_token, static_tokens)
      if event.type == SPAWN_EVENT:
          new_token=token_gen.spawn_token()
          moving_token=new_token
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
          moving_token.rotate(90)
        if event.key == pygame.K_2:
          moving_token.rotate(-90)
        if event.key == pygame.K_RIGHT:
          moving_token.move(BOX_WIDTH,0)
        if event.key == pygame.K_LEFT:
          moving_token.move(-BOX_WIDTH,0)
        if event.key == pygame.K_DOWN:
          moving_token.move(0, BOX_WIDTH)

    
    draw_window(moving_token, static_tokens)


if __name__ == '__main__':
    main()

  
