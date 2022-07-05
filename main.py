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


def handle_keyboard_movement(keys_pressed, moving_token):
  if keys_pressed[pygame.K_LEFT] and moving_token.x - BOX_WIDTH >= 0:
    moving_token.move(-BOX_WIDTH, 0)
  if keys_pressed[pygame.K_RIGHT] and moving_token.x + moving_token.width + BOX_WIDTH <= BORDER.width:
    moving_token.move(BOX_WIDTH,0)
  if keys_pressed[pygame.K_DOWN] and moving_token.y + moving_token.height + BOX_HEIGHT <= BORDER.height:
    moving_token.move(0,BOX_HEIGHT)

def main():

  # Initialization stuff
  clock = pygame.time.Clock()
  pygame.time.set_timer(TICK_EVENT, 1000)
  tick_counter=0
  running = True
  token_gen = TokenGenerator(BOX_WIDTH, BOX_HEIGHT, WIDTH)
  static_tokens=list()
  moving_token = token_gen.spawn_token()

  while running:
    clock.tick(FPS)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      if event.type == TICK_EVENT:
        tick_counter += 1
        print(f'Tick {tick_counter}')
        move_token(moving_token, static_tokens)
        keys_pressed = pygame.key.get_pressed()
        handle_keyboard_movement(keys_pressed, moving_token)
      if event.type == SPAWN_EVENT:
          new_token=token_gen.spawn_token()
          moving_token=new_token
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
          moving_token.rotate(90)
        if event.key == pygame.K_2:
          moving_token.rotate(-90)

    draw_window(moving_token, static_tokens)


if __name__ == '__main__':
    main()


