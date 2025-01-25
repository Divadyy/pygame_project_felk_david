import pygame

pygame.init()

all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

pygame.mixer.music.set_volume(100)

TILE_WIDTH = 64
TILE_HEIGHT = 64
SIZE = WIDTH, HEIGHT = 1920, 1080
LEVELS_LIST = ['levels/level_easy.txt',
               'levels/level_hard.txt']
FPS = 60
STEP = 64

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
