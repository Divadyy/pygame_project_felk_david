import pygame

pygame.init()

VOLUME = 100
pygame.mixer.music.set_volume(VOLUME)

TILE_WIDTH = 64
TILE_HEIGHT = 64
SIZE = WIDTH, HEIGHT = 1920, 1080
LEVEL_FILE = ['levels/level_1.txt',
              'levels/level_2.txt',
              'levels/level_3.txt',
              'levels/level_4.txt',
              'levels/level_5.txt',
              'levels/level_6.txt',
              'levels/level_7.txt',
              'levels/level_8.txt',
              'levels/level_9.txt',
              'levels/level_10.txt']
FPS = 60
STEP = 64
TILES_IMAGES = {'w': pygame.image.load('textures/wall64x64.png'),
                'f': pygame.image.load('textures/floor64x64.png'),
                'g': pygame.image.load('textures/entrance64x64.png'),
                'x': pygame.image.load('textures/exit64x64.png'),
                'p': pygame.image.load('textures/player64x64.png'),
                'h': pygame.image.load('textures/health64x64.png'),
                's': pygame.image.load('textures/attack64x64.png'),
                'a': pygame.image.load('textures/defense64x64.png'),
                'e': pygame.image.load('textures/skeleton64x64.png')}

GAME_OVER = pygame.image.load('menu_imgs/game_over.png')
GAME_WIN = pygame.image.load('menu_imgs/you_win.png')
CURSOR = pygame.image.load('menu_imgs/cursor.png')

clock = pygame.time.Clock()
