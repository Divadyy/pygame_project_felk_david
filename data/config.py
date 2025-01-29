import pygame

pygame.init()

all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

pygame.mixer.music.set_volume(100)

TILE_WIDTH = 64
TILE_HEIGHT = 64
SIZE = WIDTH, HEIGHT = 1920, 1080
LEVEL_FILE = 'levels/level_hard.txt'
FPS = 60
STEP = 64
TILES_IMAGES = {'w': pygame.image.load('textures/wall.png'),
                'f': pygame.image.load('textures/floor.png'),
                'v': pygame.image.load('textures/void.png'),
                'i': pygame.image.load('textures/door_cl.png'),
                'j': pygame.image.load('textures/door_op.png'),
                'd': pygame.image.load('textures/door_bs.png'),
                'g': pygame.image.load('textures/entrance.png'),
                'e': pygame.image.load('textures/exit.png'),
                'p': pygame.image.load('textures/player.png')}

FONT = pygame.font.Font(None, 8)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
